from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse 
from .forms import AgregarEstudiante, CrearGrupo, CreateUserForm
from .models import Estudiante, Facultades, Grupo
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.urls import reverse_lazy
from django.views.generic import *
# Create your views here.

# Vistas de Usuario

def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                group = form.cleaned_data['groups']
                user = form.save(commit=False)
                user.save()
                user.groups.add(group)
                messages.success(request, 'Usuario '+user.username+ ' creado exitosamente')
                return redirect('login')
            else:
                return render(request, 'register.html', {'form': form})
        else:
            form = CreateUserForm()
            return render(request, 'register.html', {'form': form})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            if (user is not None):
                login(request, user)
                return redirect ('/home/', {'user': user})
            else:
                messages.info(request, 'Usuario o contrasena incorrectos.')
        return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect ('/login/')

def perfilview(request, name):
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
        print (group, request.user.id)
    else:
        group = "Sin Rol"
    
    userprofile= User.objects.get(username=name)
    userprofilegroup = userprofile.groups.all()[0]
    estudiante = Estudiante.objects.filter(user=userprofile).first()
    if estudiante is None:
        estudiante = "NoEstudiante"    
    user = request.user
    context = {'user': user, 'name': name, 'group':group, 'estudiante':estudiante,'userprofile':userprofile,'userprofilegroup':userprofilegroup,}
    return render(request, 'perfil.html', context)

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin'])
def usuariolist(request):
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
    else:
        group = "Sin Rol"
    users = User.objects.all()
    grouplist={}
    for user in users:
        if user.groups.all().exists():
            grouplist[user.id]=user.groups.all()[0]
        else:
            grouplist[user.id]=('Sin Rol')
    print(grouplist)
    print(users)
    context = {'group':group,'users':users,'grouplist':grouplist}
    return render(request, 'users.html', context)
@login_required (login_url='/login/')
def home(request):
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
        print (group, request.user.id)
    else:
        group = "Sin Rol"
    cantfacultad = Facultades.objects.count()
    cantgrupos = Grupo.objects.count()
    cantestudiantes = Estudiante.objects.count()
    context = {'cantfacultad': cantfacultad, 'cantgrupos': cantgrupos, 'cantestudiantes': cantestudiantes, 'group': group,}
    return render(request, 'home.html',context)

# Vistas de Estudiante

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def estudiantex(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante_json = serializers.serialize('json', [estudiante])
    return JsonResponse(estudiante_json, safe=False)

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def estudiante(request):
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
    else:
        group = "Sin Rol"
    estudiantes = Estudiante.objects.all()
    context = {'estudiantes': estudiantes, 'group':group}
    return render(request, 'Estudiante/student.html', context)

# Vistas de Facultad

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def facultadx(request,id):
    grupos = Grupo.objects.filter(facultad=id)
    context = {'grupos': grupos, 'facultad': Facultades.objects.get(id=id)} 
    return render(request,'Grupo/grupo.html', context)

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def facultad(request):
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
    else:
        group = "Sin Rol"
    facultades = Facultades.objects.all()
    context = {'group':group,'facultades':facultades}
    return render(request, 'Facultad/facultad.html', context)

# Vistas de Grupos

@require_POST
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def actualizar_grupos(request):
    id_facultad = request.POST.get('facultad_id')
    grupos = Grupo.objects.filter(facultad_id=id_facultad).values('id', 'nombre')
    return JsonResponse({'grupos': list(grupos)})

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def grupox(request, id):
    estudiantes=Estudiante.objects.filter(grupo=id)
    context = {'estudiantes': estudiantes, 'grupo': Grupo.objects.get(id=id)} 
    return render(request, 'Estudiante/student.html', context)

@login_required (login_url='/login/')
@allowed_users (allowed_roles = ['Admin','Profesor','Estudiante','Secretaria'])
def grupo(request):
    if request.user.groups.all().exists():
        group = request.user.groups.all()[0].name
    else:
        group = "Sin Rol"
    grupos = Grupo.objects.all()
    context = {'group': group,'grupos': grupos}
    return render(request, 'Grupo/grupo.html', context)

class GrupoCreateView(CreateView):
    model = Grupo
    form_class = CrearGrupo
    template_name = 'Grupo/creargrupo.html'
    success_url = reverse_lazy('grupo') 

class GrupoDeleteView(DeleteView):
    model = Grupo
    template_name = 'Grupo/borrargrupo.html'
    success_url = reverse_lazy('grupo')

class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = AgregarEstudiante
    template_name = 'Estudiante/modalestudiante.html'
    success_url = reverse_lazy('estudiante')

    def form_valid(self, form):
        print("Grupo:", form.cleaned_data['grupo'] )
        print("Facultad: ", form.cleaned_data['facultad'] )
        print("aaaaaaaaaaaaaa")
        grupo = Grupo.objects.get(nombre=form.cleaned_data['grupo'], facultad=form.cleaned_data['facultad'])
    
        form.instance.grupo = grupo
        return super().form_valid(form)


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'Estudiante/borrarestudiante.html'
    success_url = reverse_lazy('estudiante')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = AgregarEstudiante
    template_name = 'Estudiante/modalestudiante.html'
    success_url = reverse_lazy('estudiante')

    def post(self, request, *args, **kwargs):
        context = super().post(request,**kwargs)
        context['estudiante'] = Estudiante.objects.filter(estado = True)
        return context
        
class UsuarioDeleteView(DeleteView):
    model = User
    template_name = 'borraruser.html'
    success_url = reverse_lazy('usuarios')

class UsuarioDetailView(DetailView):
    model = User
    form_class = User
    template_name = 'perfiluser.html'

    def get_context_data(self, **kwargs):
        if self.request.user.groups.all().exists():
            group = self.request.user.groups.all()[0].name
            print (group, self.request.user.id)
        else:
            group = "Sin Rol"
        context = super().get_context_data(**kwargs)
        user = self.request.user
        name = user.username
        userprofile= User.objects.get(username=name)
        userprofilegroup = userprofile.groups.all()[0]
        estudiante = Estudiante.objects.filter(user=userprofile).first()
        if estudiante is None:
            estudiante = "NoEstudiante"    
        context = {'user': user, 'name': name, 'group':group, 'estudiante':estudiante,'userprofile':userprofile,'userprofilegroup':userprofilegroup,}
 