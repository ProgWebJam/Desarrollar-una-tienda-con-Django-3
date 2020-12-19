from django.urls import path
#from .views import registro
from .views import VistaRegistro

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
]