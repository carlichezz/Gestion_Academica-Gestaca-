# Generated by Django 5.0.3 on 2024-03-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0002_alter_facultades_cantgrupos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultades',
            name='cantgrupos',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='cantestudiantes',
            field=models.IntegerField(default='0'),
        ),
    ]
