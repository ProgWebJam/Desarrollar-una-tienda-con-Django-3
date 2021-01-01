from django.shortcuts import redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart

# agregar productos
@login_required(login_url="/autenticacion/login")
def add_product(request, products_id):
    cart = Cart(request)
    Product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("listado_productos")

#Remover productos.
@login_required(login_url="/autenticacion/login")
def remove_product(request, products_id):
    cart = Cart(request)
    Product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("listado_productos")

#Decrementar productos.
@login_required(login_url="/autenticacion/login")
def decrement_product(request, products_id):
    cart = Cart(request)
    Product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("listado_productos")

#Limpiar el carrito de compra completo.
@login_required(login_url="/autenticacion/login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("listado_productos")