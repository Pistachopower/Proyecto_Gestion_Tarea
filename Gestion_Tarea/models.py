
from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.TextField()
    correoElectronico = models.CharField(max_length=100, unique=True) #Texto y  único
    contrasena = models.TextField()
    fecha_Registro = models.DateTimeField(default=timezone.now)
    
class Proyecto(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.TextField()
    duracion_Estimada= models.FloatField()
    fecha_Inicio= models.DateField()
    fecha_Finalizacion= models.DateField()
    usuario= models.ManyToManyField(Usuario, through='Usuario_Proyecto')   
 
 #tabla intermedia usuario proyecto
class Usuario_Proyecto(models.Model):
    #ponemos las claves foraneas de usuario y tarea
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto= models.ForeignKey(Proyecto, on_delete=models.CASCADE)    

class Tarea(models.Model):
    titulo=  models.CharField(max_length=100)
    descripcion= models.TextField()
    prioridad= models.IntegerField()
    ESTADO= [#esto es una tupla con el primer parametro para la bd y el otro para el usuario
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ] 
    
    estado= models.CharField(max_length=50,choices=ESTADO)
    
    completada= models.BooleanField()
    fecha_Creacion= models.DateField()
    hora_Vencimiento= models.TimeField()
    #indicamos la tabla intermedia entre  usuario y tarea
    usuario= models.ManyToManyField(Usuario, through='Asignacion_Tarea')
    proyecto= models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    

#creamos tabla intermedia de usuario tarea
class Asignacion_Tarea(models.Model):
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea= models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones= models.TextField()
    
class Etiqueta(models.Model):
    nombre= models.CharField(max_length=100, unique=True)
    tarea= models.ManyToManyField(Tarea, through='Tarea_Etiqueta')

#tabla intermedia tarea etiqueta
class Tarea_Etiqueta(models.Model):
    tarea= models.ForeignKey(Tarea,on_delete=models.CASCADE)
    etiqueta= models.ForeignKey(Etiqueta,on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido= models.TextField()
    fecha_Comentario= models.DateTimeField(default=timezone.now) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    asignacion_tarea = models.ForeignKey(Asignacion_Tarea, on_delete=models.CASCADE, null=True, blank=True)  
  


