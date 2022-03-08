import email
from string import digits
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Aluno(AbstractUser):
    usename = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=8, blank=True)
    matricula = models.IntegerField(unique=True, null=True)
    email = models.EmailField(null=True, blank=True)
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def get_absolute_url(self):
        return reverse('home')

class Nota(models.Model):
    disciplina = models.CharField(max_length= 50, verbose_name="Disciplina")
    nota1 = models.DecimalField(max_digits=3, blank=True, decimal_places=2, verbose_name="Nota 1")
    nota2 = models.DecimalField(max_digits=3, blank=True, decimal_places=2, verbose_name="Nota 2")
    nota3 = models.DecimalField(max_digits=4, blank=True, decimal_places=2, verbose_name="Nota 3")
    # media = models.MediaField(blank=True, verbose_name="Media")
    
