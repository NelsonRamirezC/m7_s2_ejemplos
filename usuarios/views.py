from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.models import Permission


# VISTA BASADA EN CLASE PARA REGISTRO
class UserRegistroView(CreateView):
    form_class =  UserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        
        response = super().form_valid(form)
        usuario = form.instance # obtenemos la istancia de la Clase User
        permiso = Permission.objects.get(codename='can_edit_clubes') # obtener permiso desde la base de datos
        usuario.user_permissions.add(permiso) # le agregamos el permiso al usuario
        usuario.save()

        messages.success(self.request, 'Registro exitoso.')
        return response
    
    

# VISTA BASADA EN CLASE PARA LOGIN
class UserLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    
    def form_valid(self, form):
        
        messages.success(self.request, 'Login exitoso.')
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return self.get_redirect_url() or self.success_url
    
    
#vista de logout
class UserLogoutView(LogoutView):
    next_page = 'index'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Ha cerrado la sesión exitosamente.')
        return super().dispatch(request, *args, **kwargs)
    