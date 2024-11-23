from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from domiciliosapp.models import Productos
from .forms import ProductosForm

def menu_vista(request):
    opciones = ['insertar', 'actualizar', 'listar']
    return render(request, 'menu.html', {'opciones': opciones})

def listar_productos(request):
    productos = Productos.objects.all()  # Obtiene todos los vehículos
    return render(request, 'listar.html', {'productos': productos})


def agregar_producto(request): 
    if request.method == 'POST': 
        form = ProductosForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'Producto agregado con éxito.') 
            return redirect('listar_productos') 
        else: 
            return render(request, 'agregar_producto.html', {'form': form}) 
    else: 
       form = ProductosForm() 
    return render(request, 'agregar_producto.html', {'form': form})

def eliminar_productos(request, producto_ID): 
    productos_a_eliminar = get_object_or_404(Productos, producto_ID=producto_ID) 
    productos_a_eliminar.delete() 
    messages.success(request, 'Producto eliminado con éxito.') 
    return redirect('listar_productos')

def actualizar_producto(request):
    if request.method == 'POST':
        producto_ID = request.POST.get('producto_ID', '').strip()  # Obtiene la identificación del formulario
        try:
            producto_a_actualizar = Productos.objects.get(producto_ID__iexact=producto_ID)
            form = ProductosForm(request.POST, instance=producto_a_actualizar)
            if form.is_valid():
                form.save()  # Guarda los cambios
                messages.success(request, 'Producto modificado con éxito.')
                return redirect('listar_productos')  # Redirige al listado de productos
        except Productos.DoesNotExist:
            messages.error(request, 'No se encontró un producto con esa identificación.')
            return redirect('actualizar_producto')  # Redirige a la misma página

    else:
        form = ProductosForm()  # Crea un formulario vacío

    return render(request, 'actualizar_producto.html', {'form': form})
