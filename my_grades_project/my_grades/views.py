from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
class Cadastro(CreateView):
    form_class = AlunoForm
    template_name = 'cadastro.html'
    
class DadosUpdate(UpdateView):
    model = Aluno
    fields = ['matricula', 'last_name', 'first_name']
    template_name = 'atualizarCadastro.html'
    success_url = reverse_lazy('home')