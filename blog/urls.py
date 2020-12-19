from django.urls import path
from .views import hola

urlpatterns = [
    path('holaMundo/', hola, name="hola" )
]