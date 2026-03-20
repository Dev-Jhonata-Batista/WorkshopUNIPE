from os import path
from django.urls import path
from .views import listar_usuarios

from django import views
from .views import atualizar_usuario, criar_usuario

urlpatterns = [
    path('listar/', listar_usuarios, name='listar_usuarios'),
    path('criar/', criar_usuario, name='criar_usuario'),
    path('editar/<int:pk>/', atualizar_usuario, name='atualizar_usuario'),
    path('deletar/<int:id>/', views.deletar_usuario, name='deletar'),
]

