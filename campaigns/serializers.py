from rest_framework import serializers
from .models import Cliente, Campagna, MetricaGiornaliera


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class CampagnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campagna
        fields = "__all__"


class MetricaGiornalieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricaGiornaliera
        fields = "__all__"
        read_only_fields = ["campagna"]  # Non lo richiede in input nell'aggiunta di una metrica alla campagna
