# Generated by Django 4.0.2 on 2022-03-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grades', '0002_usuario_tipousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Aluno'), (2, 'Professor')], default=1, verbose_name='Grupo'),
        ),
    ]