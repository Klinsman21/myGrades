# Generated by Django 4.0.2 on 2022-03-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
