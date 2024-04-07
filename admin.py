from django.contrib import admin
from .models import Facultades, Estudiante, Grupo
#Register your models here.
admin.site.register(Estudiante)
admin.site.register(Grupo)
admin.site.register(Facultades)
