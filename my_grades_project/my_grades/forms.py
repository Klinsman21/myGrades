from re import L
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
 
class AlunoForm(UserCreationForm):
    # username = forms.CharField(max_length=100)
    # password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    # password2 = forms.CharField(label="Password2", widget=forms.PasswordInput)
    matricula = forms.IntegerField(label="Matricula", widget=forms.NumberInput)
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    
    def _init_(self, *args, **kwargs):
        super(UserCreationForm, self)._init_(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = Aluno
        fields = ('username', 'matricula', 'email')