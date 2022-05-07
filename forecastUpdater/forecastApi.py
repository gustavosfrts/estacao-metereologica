import requests
from sensores.models import Bmp280, Dht11
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from bmp280 import BMP280
import os
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

def _get_sensors_values():
    
    sensor = Adafruit_DHT.DHT11
    GPIO.setmode(GPIO.BOARD)
    pino_sensor = 25
    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)
    retorno = []

    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)

    if umid is not None and temp is not None:
        retorno.append(temp)
        retorno.append(umid)
        retorno.append(bmp280.get_temperature())
        retorno.append(bmp280.get_pressure())
        
        return retorno
    else:
        raise Exception("Erro ao ler sensores.")
    

      
def update_sensors_values():
    retorno = _get_sensors_values()
    if retorno is not None:
        try:
            dht_11 = Dht11()
            bmp_280 = Bmp280()
            
            dht_11.temperatura = retorno[0]
            dht_11.umidade = retorno[1]
            
            bmp_280.temperatura = round(retorno[2], 2)
            bmp_280.pressao = round(retorno[3], 2)
            
            dht_11.save()
            bmp_280.save()

        except:
            pass