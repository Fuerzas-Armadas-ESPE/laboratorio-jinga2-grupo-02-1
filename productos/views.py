from django.shortcuts import render , redirect, get_object_or_404
from .models import Producto

productos = []

def listar_productos(request):
    # Consulta a la base de datos
    # Renderiza la plantilla listar.html
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def base(request):
    return render(request, 'base.html')

def crear(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        Producto.objects.create(nombre=nombre, precio=precio, cantidad=cantidad)
        return render(request, 'base.html', {'mensaje': 'Producto creado correctamente'})
    return render(request, 'crear.html')

def editar(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        producto.nombre = nombre
        producto.precio = precio
        producto.cantidad = cantidad
        producto.save()
        return render(request, 'base.html', {'mensaje': 'Producto editado correctamente'})
    return render(request, 'editar.html', {'producto': producto})

def listar_editar(request):
    productos = Producto.objects.all()
    return render(request, 'listar_editar.html', {'productos': productos})

def eliminar(request):
    productos = Producto.objects.all()
    return render(request, 'eliminar.html', {'productos': productos})

def eliminar_elemento(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('eliminar_productos')