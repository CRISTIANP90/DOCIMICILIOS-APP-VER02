from django.db import models

# Create your models here.
 
class Cliente(models.Model):
    cliente_id = models.CharField(max_length=60, primary_key="True", unique="True")
    Nombre = models.CharField(max_length=60)
    Direccion = models.CharField(max_length=60)
    Ciudad = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=20)
 
 
class Pedidos(models.Model):
    pedido_id = models.CharField(max_length=60, primary_key="True", unique="True")
    ID_cliente = models.CharField(max_length=60)
    ID_producto = models.CharField(max_length=60)
    ID_met_pago = models.CharField(max_length=60)
    ID_domiciliario = models.CharField(max_length=60)
    Fecha_de_Pedido = models.CharField(max_length=60)
    Precio_de_Pedido = models.CharField(max_length=60)
 
class Metodo_de_Pago(models.Model):
 
    Met_pago_ID = models.CharField(max_length=60, primary_key="True", unique="True")
    Precio_ped =  models.CharField(max_length=60)
    Modo_de_Pago = models.CharField(max_length=60)
    Estado_de_Pago = models.CharField(max_length=60)
 
class distri_prod(models.Model):
 
    Distribu_ID = models.CharField(max_length=60, primary_key="True", unique="True")
    NombreD =  models.CharField(max_length=60)
    Tipo_distribu = models.CharField(max_length=60)
    Ubicacion = models.CharField(max_length=60)
 
class Productos (models.Model):
 
    producto_ID = models.CharField(max_length=60, primary_key="True", unique="True")
    Nombre_pro =  models.CharField(max_length=60)
    Cantidad_pro = models.CharField(max_length=60)
    Precio_pro = models.CharField(max_length=60)
    ID_distribu = models.CharField(max_length=60)
 
class Domiciliario(models.Model):
 
    Domiciliario_ID = models.CharField(max_length=60, primary_key="True", unique="True")
    Nombre_dom =  models.CharField(max_length=60)
    Telefono_Dom = models.CharField(max_length=60)
    Disponible = models.CharField(max_length=60)
 