from django.db import models

# Create your models here.

class Substance(models.Model):
    atomic_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    symbol= models.CharField(max_length=500)
    appearance = models.CharField(max_length=100, blank=True, null=True)
    atomic_mass = models.FloatField(default=0.0)
    boil = models.FloatField(default=0.0, blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    density = models.FloatField(default=0.0)
    discovered_by = models.CharField(max_length=500, blank=True, null=True)
    melt = models.FloatField(default=0.0, blank=True, null=True)
    molar_heat = models.FloatField(default=0.0, blank=True, null=True)
    named_by = models.CharField(max_length=500, blank=True, null=True)
    period = models.IntegerField(default=0)
    phase= models.CharField(max_length=500)
    characteristics= models.TextField(default="Not Avaiavle", blank=True, null=True)

    def __str__(self):
        return self.name