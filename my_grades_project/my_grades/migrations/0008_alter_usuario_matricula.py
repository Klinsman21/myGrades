# Generated by Django 4.0.2 on 2022-03-17 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_grades', '0007_alter_usuario_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.IntegerField(unique=True),
        ),
    ]