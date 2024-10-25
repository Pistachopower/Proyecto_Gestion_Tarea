from django.shortcuts import render
from django.db.models import Q
from .models import Proyecto, Tarea, Proyecto, Usuario, Asignacion_Tarea

# Create your views here.
def index(request):
    return render(request, 'index.html')


#Crea una URL que muestre una lista de todos los proyectos
# de la aplicación con sus datos correspondientes.
def mostrar_Proyecto(request):
    proyecto= Proyecto.objects.prefetch_related('usuario').all()
    #proyecto= proyecto.all()
    return render(request, 'Proyecto/listaProyecto.html', {'mostrar_Proyecto':proyecto})

"""
Crear una URL que muestre todas las tareas que están asociadas a un
proyecto, ordenadas por fecha de creación descendente.
"""
def tareas_Proyecto(request):
    tareasAsoPro= Tarea.objects.select_related('proyecto')
    tareasAsoPro= tareasAsoPro.order_by('-Fecha_Creación')
    return render(request, 'TareaProyecto/tareaProyecto.html', {'tareas_Proyecto':tareasAsoPro})



"""
Crear una URL que muestre todos los usuarios que están asignados a una tarea 
ordenados por la fecha de asignación de la tarea de forma ascendente. 
"""
def usuario_Tarea(request,tarea_id):
    tarea= Tarea.objects.get(id= tarea_id)
    usuarioTarea= Asignacion_Tarea.objects.filter(tarea= tarea).select_related('usuario').order_by('fecha_asignacion')
    return render(request, 'UsuarioTarea/UsuarioTarea.html', {'usuario_Tarea':usuarioTarea})
