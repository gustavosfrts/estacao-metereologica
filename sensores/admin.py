from django.contrib import admin
from .models import Bmp280, Dht11

@admin.register(Dht11)
class Dht11Admin(admin.ModelAdmin):
    list_display = ('temperatura', 'umidade', 'created_at')

@admin.register(Bmp280)
class Bmp280Admin(admin.ModelAdmin):
    list_display = ('temperatura', 'pressao', 'created_at')