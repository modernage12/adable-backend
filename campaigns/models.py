from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Campagna(models.Model):
    nome = models.CharField(max_length=150)
    piattaforma = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="campagne")

    def __str__(self):
        return self.nome


class MetricaGiornaliera(models.Model):
    data = models.DateField()
    spesa = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    lead = models.PositiveIntegerField()
    conversioni = models.PositiveIntegerField()
    ricavi = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    campagna = models.ForeignKey(Campagna, on_delete=models.CASCADE, related_name="metriche")

    def __str__(self):
        return f"{self.data} | {self.campagna}"
