from django import forms
from django.forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class AgregarEstudiante(ModelForm):

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'correo', 'user', 'grupo', 'facultad', 'ci']

        labels = {

            'nombre':'Nombre',
            'apellido':'Apellido',
            'correo':'Correo',
            'user':'User', 
            'grupo':'Grupo',
            'facultad':'Facultad',
            'ci':'Ci'

        }

        widgets = {
            'grupo': TextInput(),
        }

class CrearGrupo(ModelForm):
    class Meta:
        model=Grupo
        fields=['nombre','facultad']

        labels = {
             
             'nombre': 'Nombre del Grupo' ,
             'facultad': 'Facultad'

        }

class CreateUserForm (UserCreationForm):
    groups = ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        widget=Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model= User
        fields = ['username', 'email', 'password1','password2','groups']