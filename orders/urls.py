from django.urls import path
#from .views import add_product, remove_product, decrement_product, clear_cart
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('process_order/', process_order, name='process_order'),
    path('me/', login_required(OrderList.as_view(), login_url='/autenticacion/acceder'), name='order_list'),
]