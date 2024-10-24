from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def index(request):
    return render(request, 'index.html')


#Crea una URL que muestre una lista de todos los proyectos
# de la aplicación con sus datos correspondientes.
def mostrar_Proyecto(request):
    proyecto= Proyecto.objects.prefetch_related('usuario')
    proyecto= proyecto.all()
    return render(request, 'Proyecto/listaProyecto.html', {'mostrar_Proyecto':proyecto})