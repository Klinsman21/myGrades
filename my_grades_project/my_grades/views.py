from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

class ControlPainel(LoginRequiredMixin, TemplateView):
    template_name = 'painel.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['notas'] = Nota.objects.filter(aluno=Usuario.objects.get(id=self.request.user.pk)).count()
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
        data = Nota.objects.filter(aluno=Usuario.objects.get(id=self.request.user.pk)).order_by('-disciplina', '-id')
        return data
    
class Endereco(CreateView):
    model = Endereco
    template_name = 'endereco.html'
    fields = ['aluno', 'rua', 'bairro', 'cep', 'numero', 'tipoResidencia']
    
    