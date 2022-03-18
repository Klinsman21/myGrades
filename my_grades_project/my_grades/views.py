from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class ControlPainel(TemplateView):
    template_name = 'painel.html'
    
    
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
    
class DadosUpdate(UpdateView):
    model = Usuario
    fields = ['matricula', 'last_name', 'first_name']
    template_name = 'atualizarCadastro.html'
    success_url = reverse_lazy('home')