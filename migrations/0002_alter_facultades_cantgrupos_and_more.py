# Generated by Django 5.0.3 on 2024-03-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultades',
            name='cantgrupos',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='cantestudiantes',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
