from django.shortcuts import render
from pprint import pprint

from .models import Bmp280, Dht11

def ultimoRetorno(request):
    dht11 = Dht11.objects.order_by('-created_at').first()
    bmp280 = Bmp280.objects.order_by('-created_at').first()
    return render(request, 'sensores/ultimo_retorno.html', {'dht11': dht11, 'bmp280': bmp280})

def historico(request):
    dht11 = Dht11.objects.all()
    bmp280 = Bmp280.objects.all()
    return render(request, 'sensores/historico_sensores.html', {'dht11s': dht11, 'bmp280s': bmp280})