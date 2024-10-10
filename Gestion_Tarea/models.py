from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    Nombre = models.TextField()
    CorreoElectronico = models.CharField(max_length=100, unique=True) #Texto y  único
    Contrasena = models.TextField()
    Fecha_Registro = models.DateTimeField(default=timezone.now)

class Tarea(models.Model):
    Titulo=  models.CharField(max_length=100)
    Descripcion= models.TextField()
    Prioridad= models.IntegerField()
    ESTADO= [#esto es una tupla 
        ('Pendiente'),('Progreso'),('Completada')
    ] 
    Completada= models.BooleanField()
    Fecha_Creación= models.DateField()
    hora_Vencimiento= models.TimeField()
    
class Proyecto(models.Model):
    Nombre= models.CharField(max_length=100)
    Descripcion= models.TextField()
    Duración_Estimada= models.FloatField()
    Fecha_Inicio= models.DateField()
    Fecha_Finalizacion= models.DateField()
    
class Etiqueta(models.Model):
    Observaciones= models.TextField() #texto largo
    Fecha_Asignacion= models.DateTimeField() #fecha y hora
    
class Asignacion_Tarea(models.Model):
    Observaciones= models.TextField()
    Fecha_Asignación= models.DateTimeField()
    
class Comentario(models.Model):
    Contenido= models.TextField()
    Fecha_Comentario= models.DateTimeField() 