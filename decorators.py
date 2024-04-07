from django.http import HttpResponse
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator (view_func):
        def wrapper_func (request, *args, **knargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                
                return view_func(request, *args, **knargs)
            else:
                return HttpResponse("Usuario no Autorizado <br> <br> <a href= '/logout/'> Cerrar Sesion </a>")
        return wrapper_func
    return decorator