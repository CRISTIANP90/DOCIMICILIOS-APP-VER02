"""
URL configuration for domicilios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import actualizar_producto,menu_vista,listar_productos, eliminar_productos, agregar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_vista, name='menu'),
    path('listar/Productos', listar_productos, name='listar_productos'),
    path('insertar/Productos', agregar_producto, name='agregar_producto'),
    path('actualizar/Productos', actualizar_producto, name='actualizar_producto'),
    path('eliminar/Productos/<int:producto_ID>/', eliminar_productos, name='eliminar_productos'),
]
