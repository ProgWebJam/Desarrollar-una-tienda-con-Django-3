from django.urls import path
#from .views import add_product, remove_product, decrement_product, clear_cart
from .views import *

urlpatterns = [
    path('process_order/', process_order, name='process_order'),
]