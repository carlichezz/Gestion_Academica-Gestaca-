from django.urls import path
from .views import  *



urlpatterns = [
path('login/',loginpage, name='login'),
path('logout/',logoutpage, name='logout'),
path('register/',register, name='register'),
path('users/',usuariolist, name='usuarios'),
path('users/delete/<int:pk>',UsuarioDeleteView.as_view(), name='borrarusuario'),
path('home/',home, name='home'),
path('perfil/<str:name>',perfilview, name='perfil'),
path('perfiluser/<int:pk>',UsuarioDetailView.as_view(), name='perfiluser'),
path('',home),

#Estudiante
path('agregarestudiante/', EstudianteCreateView.as_view(), name='addstudent'),
path('estudiante/',estudiante, name='estudiante'),
path('estudiante/<int:id>', estudiantex),
path('estudiante/borrar/<int:pk>', EstudianteDeleteView.as_view(), name='borrarestudiante'),
path('estudiante/update/<int:pk>', EstudianteUpdateView.as_view(), name='actualizarestudiante'),

#Grupo
path('grupo/',grupo, name='grupo'),
path('creargrupo/', GrupoCreateView.as_view(), name='creargrupo'),
path('grupo/<int:id>', grupox, name= 'grupox'),
path('grupo/borrar/<int:pk>', GrupoDeleteView.as_view(), name= 'borrargrupo'),
path('actualizar_grupos/', actualizar_grupos, name='actualizar_grupos'),

#Facultad
path('facultad/', facultad),
path('facultad/<int:id>', facultadx)

]