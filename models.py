from django.db import models
from django.db.models import Count
# Create your models here.

class Facultades (models.Model):
    nombre = models.CharField (max_length = 100)
    cantgrupos = models.IntegerField(default=0)
    
    def __str__ (self):
        return self.nombre
    
    def addgrupo (self):
        self.cantgrupos+=1
        self.save()

    def quitargrupo (self):
        self.cantgrupos-=1
        self.save()

class Grupo (models.Model):
    nombre = models.CharField(max_length =100)
    facultad = models.ForeignKey(Facultades, on_delete=models.CASCADE)
    cantestudiantes = models.IntegerField(default=0)
    

    def __str__(self):
        return self.nombre
    
    def addestudiante (self):
        self.cantestudiantes+=1
        self.save()
        self.refresh_from_db()

    def quitarest (self):
        if self.cantestudiantes > 0:
            self.cantestudiantes-=1
            self.save()
            self.refresh_from_db()

    @classmethod
    def actualizar_cantestudiantes(cls):
        grupos_con_cantestudiantes = cls.objects.annotate(cantestudiantes_anotado=Count('estudiante'))
        for grupo in grupos_con_cantestudiantes:
            grupo.cantestudiantes = grupo.cantestudiantes_anotado
            grupo.save()


class Estudiante(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    user = models.CharField(max_length = 50, unique = True)
    correo = models.CharField(max_length = 100, unique = True)
    ci = models.CharField(max_length = 11, unique = True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    facultad = models.ForeignKey(Facultades, on_delete=models.CASCADE, default=7)

    def __str__(self):
        return str(self.grupo) + '  ' + self.nombre + ' ' + self.apellido