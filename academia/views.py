from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Curso, Estudiante



# Create your views here.

def matricular(request, estudiante_id):
    contexto = {}
    
    try:
        estudiante = Estudiante.objects.get(id=estudiante_id)
        
    except estudiante.DoesNotExist:
        messages.error(request, f"No existe el estudiante con id: {estudiante_id}")
        return redirect('index')
    
    contexto["estudiante"] = estudiante
    
    if request.method == 'POST':
        # print(request.POST.get("cursos"))
        
        cursos_seleccionados_template = request.POST.getlist("cursos")
        
        cursos_inscritos = estudiante.cursos.values_list("id", flat=True)
        
        
        # print("cursos seleccionados", cursos_seleccionados)
        #print("cursos inscritos", cursos_inscritos) #<QuerySet [2, 3, 1]>
        
        # ASIGNA AL ESTUDIANTES LOS CURSOS SELECCIONADOS (CHECKED QUE NO TIENE)
        for curso_id in cursos_seleccionados_template:
            if int(curso_id) not in cursos_inscritos:
                curso = Curso.objects.get(id=curso_id)
                estudiante.cursos.add(curso)
        
        for curso_id in cursos_inscritos:
            if str(curso_id) not in cursos_seleccionados_template:
                curso = Curso.objects.get(id=curso_id)
                estudiante.cursos.remove(curso)
                
        estudiante.save()
        
        return redirect("matricular", estudiante_id=estudiante_id)
                
    else:
        
        cursos_disponibles = Curso.objects.exclude(id__in=estudiante.cursos.values_list('id', flat=True))
        
        contexto["cursos_disponibles"] = cursos_disponibles
        contexto["cursos_inscritos"] = estudiante.cursos.all()
        
        return render(request, "academia/matricular.html", contexto)