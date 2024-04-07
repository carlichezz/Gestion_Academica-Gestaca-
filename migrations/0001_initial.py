# Generated by Django 5.0.3 on 2024-03-13 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facultades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantgrupos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantestudiantes', models.CharField(max_length=100)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.facultades')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50, unique=True)),
                ('correo', models.CharField(max_length=100, unique=True)),
                ('ci', models.CharField(max_length=11, unique=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.grupo')),
            ],
        ),
    ]
