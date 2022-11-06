from tabnanny import verbose
from django.db import models

# Create your models here.
class Directores(models.Model):
    nombre=models.CharField(max_length=50,verbose_name="Nombre del Director")
    fecha_nacimiento=models.DateField(blank=True,null=True,verbose_name="Fecha de Nacimiento")

    def __str__(self):
        return f'nombre: {self.nombre}, Fecha de Nacimiento: {self.fecha_nacimiento}'

class Peliculas(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True,null=True)
    tipo=models.CharField(max_length=50)
    director=models.ForeignKey(Directores,on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return f'nombre: {self.nombre}, tipo: {self.tipo}'