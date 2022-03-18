import email
from string import digits
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.urls import reverse




class Usuario(AbstractUser):
    tipos = (
          (1, 'Aluno'),
          (2, 'Professor'),
    )
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8, blank=True)
    matricula = models.CharField(unique=True, max_length=7)
    email = models.EmailField(null=True, blank=True, unique=True)
    tipoUsuario = models.PositiveSmallIntegerField(blank=True, default=1, choices=tipos, verbose_name="Grupo")
    # group = models.ForeignKey(Group, blank=False, default=1, verbose_name="Grupo", on_delete=models.CASCADE)
    
    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['username']
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def get_absolute_url(self):
        return reverse('painel')
    
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
        return self.disciplina.nome
    

class Endereco(models.Model):
    tipos=(
        (1, 'Rural'),
        (2, 'Urbano')
    )
    aluno = models.ForeignKey(Usuario, related_name='Aluno', on_delete=models.CASCADE, blank=False)
    rua = models.CharField(max_length=100, blank=False, verbose_name='Rua')
    bairro = models.CharField(max_length=50, blank=False, verbose_name='Bairro')
    cep = models.CharField(max_length=50, blank=False, verbose_name='CEP')
    numero = models.PositiveSmallIntegerField(default=0, verbose_name='Numero da residência')
    tipoResidencia = models.PositiveSmallIntegerField(choices=tipos, blank=False, verbose_name='Tipo da residência', default=2)

    
