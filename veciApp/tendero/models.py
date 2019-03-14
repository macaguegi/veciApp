# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete='CASCADE')

    #additional
    web_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username



class Categoria(models.Model):
    k_categoria = models.CharField(primary_key=True, max_length=50)
    n_nombre = models.CharField(max_length=50)
    n_descripcion = models.CharField(max_length=250, blank=True, null=True)
    k_identificaciont = models.DecimalField(max_digits=65535, decimal_places=65535)
    k_tipoidt = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'categoria'


class Cliente(models.Model):
    k_identificacion = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    k_tipoid = models.CharField(max_length=2)
    n_nombre = models.CharField(max_length=50)
    n_apellido = models.CharField(max_length=50)
    o_email = models.CharField(max_length=50)
    o_celular = models.CharField(max_length=50)
    o_telefono = models.CharField(max_length=50, blank=True, null=True)
    o_direccion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('k_identificacion', 'k_tipoid'),)


class Detalle(models.Model):
    k_detalle = models.CharField(primary_key=True, max_length=50)
    q_cantidad = models.DecimalField(max_digits=65535, decimal_places=65535)
    v_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535)
    k_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='k_orden')
    k = models.ForeignKey('Producto', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'detalle'


class Orden(models.Model):
    k_orden = models.CharField(primary_key=True, max_length=50)
    k_identificacion = models.ForeignKey('Tienda', models.DO_NOTHING, db_column='k_identificacion')
    f_orden = models.DateField()
    k_tipoid = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'orden'


class Producto(models.Model):
    k_id = models.CharField(primary_key=True, max_length=50)
    n_nombre = models.CharField(max_length=50)
    n_descripcion = models.CharField(max_length=250, blank=True, null=True)
    v_precio = models.DecimalField(max_digits=65535, decimal_places=65535)
    k_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='k_categoria')

    class Meta:
        managed = False
        db_table = 'producto'


class Tendero(models.Model):
    k_identificacion = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    k_tipoid = models.CharField(max_length=2)
    n_nombre = models.CharField(max_length=50)
    n_apellido = models.CharField(max_length=50)
    o_email = models.CharField(max_length=50)
    o_celular = models.CharField(max_length=50)
    o_telefono = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tendero'
        unique_together = (('k_identificacion', 'k_tipoid'),)


class Tienda(models.Model):
    k_identificaciont = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    k_tipoidt = models.CharField(max_length=2)
    n_nombre = models.CharField(max_length=50)
    o_direccion = models.CharField(max_length=100)
    k_identificacion = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    k_tipoid = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tienda'
        unique_together = (('k_identificaciont', 'k_tipoidt'),)
