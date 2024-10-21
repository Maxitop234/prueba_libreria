from django.db import models
class Autor(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre del autor')
    biografia=models.TextField(max_length=100,verbose_name='biografia')
    fnacimiento = models.DateTimeField(verbose_name='fecha nacimiento')
    nacionalidad = models.CharField(max_length=100, verbose_name='nacionalidad')
    estado = models.IntegerField(verbose_name='estado')
    class Meta:
        db_table = 'Autor'
    def __str__(self):
        return self.nombre
    
    

class Idioma(models.Model):
    nombre_idioma=(models.CharField(max_length=100,verbose_name='nombre de idioma'))
    class Meta:
         db_table = 'Idioma'
    def __str__(self):
        return self.nombre_idioma

class Editorial(models.Model):
    nombre_editorial = (models.CharField(max_length=100, verbose_name='nombre de la Editorial'))
    class Meta:
         db_table = 'Editorial'
    def __str__(self):
        return self.nombre_editorial


class Rol(models.Model):
    nombre_rol = (models.CharField(max_length=100,verbose_name='nombre del rol'))
    class Meta:
         db_table = 'Rol'
    def __str__(self):
        return self.nombre_rol
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    correo = models.CharField(max_length=100, verbose_name='correo')
    password = models.CharField(max_length=100,verbose_name='contraseña')
    created = models.DateTimeField(verbose_name='fecha de creacion', auto_now=True)
    updated = models.DateTimeField(verbose_name='fecha de actualizacion',auto_now=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado = models.IntegerField(verbose_name='estado')
    class Meta:
        db_table = 'Usuario'
    def __str__(self):
        return self.nombre

class Libros(models.Model):
    titulo = models.CharField(max_length=100,verbose_name='titulo de libro')
    id_autor = models.ForeignKey(Autor,verbose_name='id autor',on_delete=models.CASCADE)
    fpublicacion = models.DateField(verbose_name='fecha de publicacion')
    id_editorial = models.ForeignKey(Editorial,verbose_name='id editorial',on_delete=models.CASCADE)
    stock = models.IntegerField(verbose_name='stock')
    nro_paginas = models.IntegerField(verbose_name='numero de paginas')
    idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE )
    estado = models.IntegerField(verbose_name='estado')
    class Meta:
        db_table = 'Libro'
    def __str__(self):
        return self.titulo


# Create your models here.
