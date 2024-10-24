from django.urls import path
from .import views

urlpatterns = [
      path('',views.index,name='index'),
      path('mostrar',views.mostrar_Proyecto,name='mostrar_Proyecto'),
      path('tarea',views.tareas_Proyecto,name='tareas_Proyecto'),
      path('usuariotarea',views.usuario_Tarea,name='usuario_Tarea'),
      
]