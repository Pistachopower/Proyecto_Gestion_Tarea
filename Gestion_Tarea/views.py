from django.shortcuts import render
from django.db.models import Q
from .models import Proyecto, Tarea, Proyecto, Usuario, Asignacion_Tarea, Comentario, Etiqueta
from django.views.defaults import page_not_found

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
    tareasAsoPro= tareasAsoPro.order_by('-fecha_Creacion')
    return render(request, 'TareaProyecto/tareaProyecto.html', {'tareas_Proyecto':tareasAsoPro})



"""
Crear una URL que muestre todos los usuarios que están asignados a una tarea 
ordenados por la fecha de asignación de la tarea de forma ascendente. 
"""
def usuario_Tarea(request):
    usuarioTarea= Asignacion_Tarea.objects.select_related('usuario', 'tarea').order_by('tarea__fecha_Creacion')
    return render(request, 'UsuarioTarea/UsuarioTarea.html', {'usuario_Tarea':usuarioTarea})

"""
Crear una URL que muestre todas las tareas que tengan un texto en concreto en las 
observaciones a la hora de asignarlas a un usuario.
"""
def tareas_Observaciones_Usuarios(request, texto):
    texto_Concreto= Asignacion_Tarea.objects.select_related('tarea', 'usuario')
    texto_Concreto= texto_Concreto.filter(observaciones__contains= texto) 
    return render(request, 'TareasObservacionesUsuarios/tareasObservacionesUsuarios.html', {'tareas_Observaciones_Usuarios':texto_Concreto})

"""
Crear una URL que muestre todos las tareas que se han creado entre dos años y el estado 
sea “Completada”.
"""
def tareas_Entre_DosAnios_Completada(request, anio1, anio2, estadoParam):
    t_dosAnios= Tarea.objects.all()
    t_dosAnios= t_dosAnios.filter(Q(fecha_Creacion__year= anio1) | Q(fecha_Creacion__year= anio2)).filter(estado= estadoParam)
    return render(request, 'TareaDosAniosCompletada/tareaDosAniosCompletada.html', {'tareas_Entre_DosAnios_Completada':t_dosAnios})

"""
Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en 
concreto.

"""
def ultimo_Usuario_Comentado_Tarea(request):
    ultimoUsuarioComentadoTarea= Comentario.objects.select_related('usuario').all()
    ultimoUsuarioComentadoTarea= ultimoUsuarioComentadoTarea.order_by('-fecha_Comentario')[:1]
    return render(request, 'Ultimo_Usuario_Comentado_Tarea/ultimo_Usuario_Comentado_Tarea.html', {'ultimo_Usuario_Comentado_Tarea':ultimoUsuarioComentadoTarea})

    
"""
Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra 
que se pase en la URL y que el año del comentario sea uno en concreto.

comentario, tarea, filter(palabra y año)
"""
def comentarios_tarea_Palabra_Anio(request, palabra, anioComentario):
    todos_Comentarios = Comentario.objects.filter(
        Q(contenido__startswith=palabra),
        fecha_Comentario__year=anioComentario) 
    
    return render(request, 'TodosComentarioTarea/todosComentarioTarea.html', {'comentarios_tarea_Palabra_Anio':todos_Comentarios})


"""
Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas 
de un proyecto.
"""
def etiquetas_Tareas_Proyecto(request, id_Proyecto):
    etiquetaTareaProyecto= Etiqueta.objects.prefetch_related('tarea').all()
    etiquetaTareaProyecto= etiquetaTareaProyecto.filter(tarea__proyecto_id=id_Proyecto)
    return render(request, 'Etiquetas_Tareas_Proyecto/etiquetas_Tareas_Proyecto.html', {'etiquetas_Tareas_Proyecto':etiquetaTareaProyecto})



"""
Crear una URL que muestre todos los usuarios que no están asignados a una tarea.
"""
def usuarios_Sin_tarea(request):
    usuarioSinTarea = Usuario.objects.filter(asignacion_tarea__isnull=True) #filtrando los usuarios que no tienen ninguna asignación de tarea asociada
    return render(request, 'Usuarios_Sin_tarea/usuarios_Sin_tarea.html', {'usuarios_Sin_tarea':usuarioSinTarea})

#vistas para los errores
def error_400(request, exception=None):
    return render(request, 'Errores/400.html', None, None, 400)

def error_403(request, exception=None):
    return render(request, 'Errores/403.html', None, None, 403)

def error_404(request, exception=None):
    return render(request, 'Errores/404.html', None, None,404)

def error_500(request, exception=None):
    return render(request, 'Errores/500.html', None, None,500)