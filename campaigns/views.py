from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import services
import csv
import io
from django.db import transaction


# Create your views here.
@api_view(['GET', 'POST'])
def lista_clienti(request):
    if request.method == "GET":
        clienti = models.Cliente.objects.all()
        serializer = serializers.ClienteSerializer(clienti, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = serializers.ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def lista_campagne(request):
    if request.method == "GET":
        campagne = models.Campagna.objects.all()
        serializer = serializers.CampagnaSerializer(campagne, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = serializers.CampagnaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def campagne_cliente(request, id):
    # Prima controllo che il cliente esista
    cliente = get_object_or_404(models.Cliente, id=id)

    # Poi ottengo QuerySet di tutte le campagne del cliente
    # .filter()/.all() invece di .get() perchè sono più di un oggetto
    campagna_cliente = cliente.campagne.all()
    serializer = serializers.CampagnaSerializer(campagna_cliente, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def metriche_campagna(request, id):
    campagna = get_object_or_404(models.Campagna, id=id)

    if request.method == "GET":
        metrica_campagna = campagna.metriche.all()
        serializer = serializers.MetricaGiornalieraSerializer(metrica_campagna, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = serializers.MetricaGiornalieraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(campagna=campagna)  # Assegno la metrica alla campagna richiesta
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def genera_report(request, id):
    campagna = get_object_or_404(models.Campagna, id=id)

    report = services.genera_report_campagna(campagna)

    return Response(report, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def dettaglio_cliente(request, id):
    """Recupera, aggiorna o elimina un cliente esistente"""
    cliente = get_object_or_404(models.Cliente, id=id)

    if request.method == 'GET':
        serializer = serializers.ClienteSerializer(cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = serializers.ClienteSerializer(cliente, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = serializers.ClienteSerializer(cliente, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def dettagli_campagna(request, id):
    """Recupera, aggiorna o elimina una campagna esistente"""
    campagna = get_object_or_404(models.Campagna, id=id)

    if request.method == 'GET':
        serializer = serializers.CampagnaSerializer(campagna)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = serializers.CampagnaSerializer(campagna, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = serializers.CampagnaSerializer(campagna, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        campagna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def dettagli_metrica(request, id):
    """Recupera, aggiorna o elimina una metrica esistente"""
    metrica = get_object_or_404(models.MetricaGiornaliera, id=id)

    if request.method == 'GET':
        serializer = serializers.MetricaGiornalieraSerializer(metrica)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = serializers.MetricaGiornalieraSerializer(metrica, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = serializers.MetricaGiornalieraSerializer(metrica, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        metrica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def importa_metriche(request, id):
    """Importa metriche da file CSV tramite richiesta HTTP"""
    campagna = get_object_or_404(models.Campagna, id=id)  # Controllo prima che la campagna esista

    file = request.FILES.get("file")  # Recupera file passato tramite richiesta HTTP
    if file is None:  # .get() ritorna None se il file non esiste
        return Response(status=status.HTTP_400_BAD_REQUEST)

    contenuto = file.read().decode("utf-8-sig")  # Trasformo il CSV in testo
    righe = csv.DictReader(io.StringIO(contenuto))  # io.StringIO() rende il testo leggibile come un file.

    lista_metriche = list(righe)

    serializer = serializers.MetricaGiornalieraSerializer(data=lista_metriche, many=True)
    serializer.is_valid(raise_exception=True)

    with transaction.atomic():  # Se il salvataggio fallisce, annulla tutte le modifiche della transazione
        serializer.save(campagna=campagna)

    return Response(serializer.data, status=status.HTTP_201_CREATED)




