from django.urls import path, include
from django.contrib.auth import views

from .views import *

urlpatterns = [
    path('', views.LoginView.as_view(), name='home'),
    path('cadastro', Cadastro.as_view(), name='cadastro'),
    path('painel', ControlPainel.as_view(), name='painel'),
    path('notas', ListaNotas.as_view(), name='notas'),
    path('endereco', Endereco.as_view(), name='endereco'),
    path('editar/<pk>/', DadosUpdate.as_view(), name='editar-campo'),

]