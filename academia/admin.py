from django.contrib import admin

# Register your models here.

from .models import Curso, Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", )
    search_fields = ("nombre", "apellido", )
    list_filter = ("cursos", )
    
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", )
    search_fields = ("nombre", "descripcion", )
    list_filter = ("nombre", )
    
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)
