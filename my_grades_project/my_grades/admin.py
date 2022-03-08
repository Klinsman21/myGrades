from django.contrib import admin
from django.contrib.auth import admin as adminUser
from django.contrib.auth import forms as adminForm
from .models import *
from .forms import AlunoForm

admin.site.register(Nota)

@admin.register(Aluno)
class AlunoAdmin(adminUser.UserAdmin):
    form = adminForm.UserChangeForm
    add_form = AlunoForm
    model = Aluno
    fieldsets = adminUser.UserAdmin.fieldsets + (
        ('Matricula', {"fields": ("matricula",)}),
    )


