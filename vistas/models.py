from django.db import models

# Create your models here.
class Tabla_test(models.Model):
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    Rol = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    ApellidoPaterno = models.CharField(max_length=200)
    ApellidoPaterno = models.CharField(max_length=200)
    Curp = models.CharField(max_length=200)
    Brithday = models.DateTimeField()
   
    
