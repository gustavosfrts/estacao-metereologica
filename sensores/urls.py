from urllib import request
from django.urls import path
from . import views

app_name = "sensores"

urlpatterns = [
    # path("", views.Dht11ListView.as_view(), name="list"),
    # path("", views.IndexListView.as_view(), name="indexList"),
    # path("", views.MultipleModelView.as_view(), name="indexList"),
    path("", views.teste, name="indexList"),
]
