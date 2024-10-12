from django.contrib import admin
from .models import Usuario, Proyecto, Usuario_Proyecto, Tarea, Asignacion_Tarea, Etiqueta,Tarea_Etiqueta, Comentario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Usuario_Proyecto)
admin.site.register(Tarea)
admin.site.register(Asignacion_Tarea)
admin.site.register(Etiqueta)
admin.site.register(Tarea_Etiqueta)
admin.site.register(Comentario)
