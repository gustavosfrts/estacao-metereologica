from django.db import models
from django.forms import DateTimeField

class Dht11(models.Model):
    temperatura = models.FloatField() #ºC
    umidade = models.FloatField() #%
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ("-created_at",)

class Bmp280(models.Model):
    temperatura = models.FloatField() #ºC
    pressao = models.FloatField() #hPa
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ("-created_at",)