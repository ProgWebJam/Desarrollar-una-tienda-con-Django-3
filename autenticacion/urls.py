from django.urls import path
#from .views import registro
from .views import VistaRegistro, salir

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('salir/',salir, name="salir"),
]