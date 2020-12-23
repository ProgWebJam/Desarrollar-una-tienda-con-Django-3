from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.forms import FormularioPost
from django.contrib import messages
from blog.models import Post

def index(request):
    post = Post.objects.all()
    return render(request,"blog.html",{"posts":post})

def crear_post(request):
    if request.method == "POST":
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get("titulo")
            messages.success(request, f"El post {titulo} se ha creado correctamente")
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])


    form = FormularioPost()
    return render(request,"crear_post.html",{"form":form})