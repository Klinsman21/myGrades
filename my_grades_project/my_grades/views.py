from ast import For
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

class ControlPainel(LoginRequiredMixin, TemplateView):
    template_name = 'painel.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['avisos'] = Aviso.objects.all().count()
        r = requests.get(url='http://localhost:3000/lerAvisos')
        print(r.json())
        return data
    

class Cadastro(CreateView):
    form_class = UsuarioForm
    template_name = 'cadastro.html'
    def form_valid(self, form):
        form.save()
        username = self.request.POST['matricula']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect('painel')
    
class DadosUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['last_name', 'first_name', 'username', 'email']
    template_name = 'atualizarCadastro.html'
    success_url = reverse_lazy('painel')

class ListaNotas(LoginRequiredMixin, ListView):
    model = Nota
    context_object_name = 'nota'
    template_name = 'notas.html'
 
    def get_queryset(self):
        periodo = self.kwargs['pr']
        data = Nota.objects.filter(aluno=Usuario.objects.get(id=self.request.user.pk)).filter(periodo=periodo).order_by('-disciplina', '-id')
        return data
    
class EnderecoLista(LoginRequiredMixin, ListView):
    model = Endereco
    context_object_name = 'endereco'
    template_name = 'enderecoList.html'
 
    def get_queryset(self):
        data = Endereco.objects.filter(aluno=Usuario.objects.get(id=self.request.user.pk))
        return data

class CadastrarEndereco(LoginRequiredMixin, CreateView):
    model = Endereco
    template_name = 'endereco.html'
    fields = ['aluno', 'rua', 'bairro', 'cep', 'numero', 'tipoResidencia']
    
    
class DeleteEndereco(LoginRequiredMixin, DeleteView):
    model = Endereco
    template_name = 'deleteEndereco.html'
    success_url ="/enderecoLista"
    

class AvisoLista(LoginRequiredMixin, ListView):
    model = Endereco
    context_object_name = 'aviso'
    template_name = 'avisosLista.html'
 
    def get_queryset(self):
        data = Endereco.objects.filter(aluno=Usuario.objects.get(id=self.request.user.pk))
        return data
    
    