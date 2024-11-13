from django.shortcuts import render
from .models import Producto, Categoria
from django.db.models import Q 
from django.db.models import Count, Sum, Avg, Min, Max
from .forms import ProductoForm
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def listado_productos(request):
    
    nombre = request.GET.get('nombre')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    fecha_vencimiento_min = request.GET.get('fecha_vencimiento_min')
    fecha_vencimiento_max = request.GET.get('fecha_vencimiento_max')
    
    if not nombre:
        nombre = ""
    
    contexto = {}
    productos = Producto.objects.all().order_by('-id')
    
    if nombre:
        productos = productos.filter(Q(nombre__icontains=nombre) | Q(descripcion__icontains=nombre))
        
    if precio_min: 
        productos = productos.filter(precio__gte=precio_min)
        
    if precio_max:
        productos = productos.filter(precio__lte=precio_max)
        
    if fecha_vencimiento_min:
        productos = productos.filter(fecha_vencimiento__gte=fecha_vencimiento_min)
        
    if fecha_vencimiento_max:
        productos = productos.filter(fecha_vencimiento__lte=fecha_vencimiento_max)
        
    # utilizamos min y max (built-in functions de python para evitar realizar más consultas a la BD)
    limite_min= min((p.fecha_vencimiento for p in productos if p.fecha_vencimiento), default=None)
    limite_max= max((p.fecha_vencimiento for p in productos if p.fecha_vencimiento), default=None)
    

    contexto["productos"] = productos
    contexto["categorias"] = Categoria.objects.all().order_by('nombre')
    contexto["nombre"] = nombre
    contexto["precio_min"] = precio_min
    contexto["precio_max"] = precio_max
    contexto["fecha_vencimiento_min"] = fecha_vencimiento_min
    contexto["fecha_vencimiento_max"] = fecha_vencimiento_max
    contexto["limite_min"] = limite_min
    contexto["limite_max"] = limite_max
    

    return render(request, 'listado_productos.html', contexto)



def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoForm()
        return render(request, 'add_producto.html', contexto)
    
    if request.method == 'POST':
        
        form = ProductoForm(request.POST)
        contexto["form"] = form 
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'add_producto.html', contexto)
        
def update_producto(request):
    contexto = {}
    return render(request, 'update_producto.html', contexto)