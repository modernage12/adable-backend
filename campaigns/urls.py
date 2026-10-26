from django.urls import path
from . import views

urlpatterns = [
    path('clienti/', views.lista_clienti, name="lista-clienti"),
    path('campagne/', views.lista_campagne, name="lista-campagne"),
    path('clienti/<int:id>/campagne/', views.campagne_cliente, name="lista-campagne-cliente"),
    path('campagne/<int:id>/metriche/', views.metriche_campagna, name="metriche-campagna"),
    path('campagne/<int:id>/report/', views.genera_report, name="genera-report"),
    path('clienti/<int:id>/', views.dettaglio_cliente, name="dettaglio-cliente"),
    path('campagne/<int:id>/', views.dettagli_campagna, name="dettagli-campagna"),
    path('metrica/<int:id>/', views.dettagli_metrica, name="dettagli-metrica"),
    path('campagne/<int:id>/importa-metriche', views.importa_metriche, name="importa-metriche")
]
