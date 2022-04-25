import requests
from sensores.models import Bmp280, Dht11

def _get_forecast_json():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    encoded_city_name = 'Sao%20Paulo'
    country_code = 'br'
    access_token = 'api_key'
  
    r = requests.get('{0}?q={1},{2}&APPID={3}'.format(
        url, 
        encoded_city_name, 
        country_code, 
        access_token))

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None

      
def update_forecast():
    json = _get_forecast_json()
    if json is not None:
        try:
            dht_11 = Dht11()
            bmp_280 = Bmp280()
            
            # open weather map gives temps in Kelvin. We want celsius.              
            temp_in_celsius = json['main']['temp'] - 273.15
            dht_11.temperatura = temp_in_celsius
            # dht_11.description = json['weather'][0]['description']
            # dht_11.city = json['name']
            dht_11.umidade = json['main']['humidity']

            bmp_280.temperatura = temp_in_celsius
            bmp_280.pressao = json['main']['pressure']
            
            dht_11.save()
            bmp_280.save()
            print("salvano...\n" + dht_11, bmp_280)
        except:
            pass