from django.shortcuts import render , redirect, get_object_or_404
from .models import Producto
from django.http import HttpResponse
import csv
from .forms import CSVUploadForm


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

def exportar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Precio', 'Stock'])  # Escribe la cabecera del CSV

    productos = Producto.objects.all().values_list('nombre', 'precio', 'cantidad')
    for producto in productos:
        writer.writerow(producto)  # Escribe los datos de cada producto

    return response

def importar_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                producto, created = Producto.objects.get_or_create(
                    nombre=row['Nombre'],
                    defaults={'precio': row['Precio'], 'cantidad': row['Stock']}
                )
                if not created:
                    producto.precio = row['Precio']
                    producto.cantidad = row['Stock']
                    producto.save()

            return redirect('listar_productos')
    else:
        form = CSVUploadForm()
    return render(request, 'importar.html', {'form': form})