from django.urls import path, include
from django.contrib.auth import views

from .views import *

urlpatterns = [
    path('', views.LoginView.as_view(), name='home'),
    path('cadastro', Cadastro.as_view(), name='cadastro'),
    
    path('editar/<pk>/', DadosUpdate.as_view(), name='editar-campo'),

]