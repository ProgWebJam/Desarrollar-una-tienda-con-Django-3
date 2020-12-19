from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
class VistaRegistro(View): 
    def get(self, request):
        form = UserCreationForm()
        return render( request,'registro.html',{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            #f = darle formato a una cadena
            messages.success(request,f"Bienvenid@ a la plataforma {nombre_usuario}")
            login(request, usuario)
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render( request,'registro.html',{"form":form})
