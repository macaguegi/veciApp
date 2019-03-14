from django.contrib import admin
from tendero.models import Categoria, Tienda, Tendero, Cliente , Orden , Detalle, Producto, UserProfileInfo
# Register your models here.


admin.site.register(Categoria)
admin.site.register(Tienda)
admin.site.register(Tendero)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Detalle)
admin.site.register(Producto)
admin.site.register(UserProfileInfo)