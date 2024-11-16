from django.shortcuts import render

def menu_vista(request):
    opciones = ['Cliente', 'Pedidos', 'Metodo de Pago', 'distribuidora de productos', 'Productos', 'Domiciliarios']
    return render(request, 'menu.html', {'opciones': opciones})
