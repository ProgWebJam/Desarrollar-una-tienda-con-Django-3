from django.urls import path
#from .views import registro
from .views import VistaRegistro, salir, acceder

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/',salir, name="salir"),
]