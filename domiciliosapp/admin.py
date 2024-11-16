from django.contrib import admin
from .models import Cliente
from .models import Pedidos
from .models import Metodo_de_Pago
from .models import distri_prod
from .models import Productos
from .models import Domiciliario
 
 
# Register your models here.
 
admin.site.register(Cliente)
admin.site.register(Pedidos)
admin.site.register(Metodo_de_Pago)
admin.site.register(distri_prod)
admin.site.register(Productos)
admin.site.register(Domiciliario)