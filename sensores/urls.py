from urllib import request
from django.urls import path
from . import views

app_name = "sensores"

urlpatterns = [
    path("", views.ultimoRetorno, name="indexList"),
    path("historico/", views.historico, name="historicoList"),
]
