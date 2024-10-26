from django.urls import path
from .import views

urlpatterns = [
      path('',views.index,name='index'),
      path('mostrar',views.mostrar_Proyecto,name='mostrar_Proyecto'),
      path('tarea',views.tareas_Proyecto,name='tareas_Proyecto'),
      path('usuariotarea',views.usuario_Tarea,name='usuario_Tarea'),
      path('observaciones/<str:texto>/',views.tareas_Observaciones_Usuarios,name='tareas_Observaciones_Usuarios'),
      path('tareaentredosanios/<int:anio1>/<int:anio2>/<str:estadoParam>',views.tareas_Entre_DosAnios_Completada,name='tareas_Entre_DosAnios_Completada'),
      path('ultimousuariocomenta/', views.ultimo_Usuario_Comentado_Tarea, name= 'ultimo_Usuario_Comentado_Tarea'),
      
      
      #    path('ultimo_usuario_comentario/<int:proyecto_id>/<int:tarea_id>/', ultimo_usuario_comentario, name='ultimo_usuario_comentario'),
]