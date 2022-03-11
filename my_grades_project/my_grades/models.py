import email
from string import digits
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Usuario(AbstractUser):
    tipos = (
          (1, 'Aluno'),
          (2, 'Professor'),
      )
    usename = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=8, blank=True)
    matricula = models.IntegerField(unique=True, null=True)
    email = models.EmailField(null=True, blank=True)
    tipoUsuario = models.PositiveSmallIntegerField(blank=True, default=1, choices=tipos, verbose_name="Grupo")
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def get_absolute_url(self):
        return reverse('home')
    
class Disciplina(models.Model):
    nome = models.CharField(max_length = 25, blank=False, verbose_name="Disciplina")
    
    def __str__(self):
        return self.nome

class Nota(models.Model):
    tipos = (
        ("P", "Prova"),
        ("T", "Trabalho"),
        ("A", "Artigo"),
        ("S", "Seminário"),
        ("O", "Outro"),
    )
    periodos = (
        (1, 1),(2, 2),
        (3, 3),(4, 4),
        (5, 5),(6, 6),
        (7, 7),(8, 8),
        (9, 9),(10, 10),
    )
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default=None, related_name="disciplina", blank=False)
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=False, default= None, related_name="aluno")
    periodo = models.PositiveSmallIntegerField(verbose_name='Periodo', choices=periodos, default=1, blank=False)
    nota = models.PositiveIntegerField(verbose_name='Nota', default=0, blank=False)
    tipo = models.CharField(max_length=50, choices=tipos, blank=False, verbose_name= 'Tipo de nota')
    
    def __str__(self):
        return self.Usuario.username + " - " + self.disciplina.nome + ": " + str(self.nota)

    
