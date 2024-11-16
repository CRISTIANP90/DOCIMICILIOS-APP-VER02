from django.shortcuts import render

def menu_vista(request):
    opciones = ['Cliente', 'Pedidos', 'Metodo de Pago', 'distribuidora de productos', 'Productos', 'Domiciliarios']
    return render(request, 'domiciliosapp/menu.html', {'opciones': opciones})
