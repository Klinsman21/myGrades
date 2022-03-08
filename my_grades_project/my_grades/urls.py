from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cadastro', Cadastro.as_view(), name='cadastro'),
    
    path('editar/<pk>/', DadosUpdate.as_view(), name='editar-campo'),

]