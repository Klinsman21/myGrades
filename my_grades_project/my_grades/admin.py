from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms as adminForm
from .models import *
from .forms import UsuarioForm

class UsuarioAdmin(UserAdmin):
    model = Usuario
    add_form = UsuarioForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Dados Escolares',
            {
                'fields': (
                    'matricula',
                    'tipoUsuario',
                )
            }
        )
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('username', 'password1', 'password2', 'email', 'matricula', 'tipoUsuario',),
        }
        ),
    )
    
admin.site.register(Nota)
admin.site.register(Disciplina)
admin.site.register(Usuario, UsuarioAdmin)