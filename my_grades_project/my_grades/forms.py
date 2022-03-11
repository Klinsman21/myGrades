from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
 
class UsuarioForm(UserCreationForm):
    tipos = (
          (1, 'Aluno'),
          (2, 'Professor'),
      )
    matricula = forms.IntegerField(label="Matricula", widget=forms.NumberInput)
    tipoUsuario = forms.ChoiceField(label="Grupo", widget=forms.RadioSelect, choices=tipos, initial= 1, required=False)
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    
    def _init_(self, *args, **kwargs):
        super(UserCreationForm, self)._init_(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = Usuario
        fields = ('username', 'matricula', 'email', 'tipoUsuario', 'first_name',)