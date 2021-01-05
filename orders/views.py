from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import rendirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Order, OrderLine
from cart.cart import Cart

# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def process_order(request):
    order = Order.objects.create(user=request.user, completd=True)
    cart = Cart(request)
    order_lines = list()
    for key, value in cart.cart.items():
        order_lines.append(
            OrderLine(
                product_id=key,
                quantity=value["quantity"],
                user=request.user,
                order=order
            )
        )
    #bulk_create= crea muchos registros de forma optimizada en la BD
    OrderLine.objects.bulk_create(order_lines)

    #Metodo para enviar correo
    messages.success(request, "El pedido se a creado correctamente!")
    return rendirect("Listado_productos")