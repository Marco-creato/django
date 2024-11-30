
from django.contrib import admin
from django.urls import path
from .views import fproduto, fcadproduto, salvar, excluir, exibir, update, celulares

urlpatterns = [
    path('', fproduto),
    path('fcadproduto/',fcadproduto, name='fcadproduto'),
    path('salvar/', salvar, name='salvar'),
    path('excluir/<int:id>',excluir, name='excluir'),
    path('exibir/<int:id>',exibir, name='exibir'),
    path('update/<int:id>',update, name='update'),
    path('celulares/', celulares, name='celulares'),

]
