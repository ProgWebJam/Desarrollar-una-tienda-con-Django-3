from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

#Registrar Usuario

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario,password=password)

            if usuario is not None:
                login(request,usuario)
                messages.success(request,f"Bienvenid@ de nuevo a la plataforma {nombre_usuario}")
                return redirect("blog")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")        

    form = AuthenticationForm
    return render(request,'acceder.html',{"form":form})

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

#Cerrar Sesion
def salir(request):
    logout(request)
    messages.success(request,f"Tu sesion se ha cerrado correctamente")
    return redirect("acceder")