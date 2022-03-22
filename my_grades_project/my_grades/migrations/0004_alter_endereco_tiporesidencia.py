# Generated by Django 4.0.2 on 2022-03-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grades', '0003_alter_endereco_tiporesidencia_alter_nota_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='tipoResidencia',
            field=models.CharField(choices=[('Rural', 'Rural'), ('Urbana', 'Urbana')], default='Urbana', max_length=7, verbose_name='Tipo da residência'),
        ),
    ]
