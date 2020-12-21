from django.urls import path
from .views import index, crear_post

urlpatterns = [
    path('', index, name="blog" ),
    path('post/crear', crear_post, name="crear_post" ),
]