from django.urls import path
from .import views

urlpatterns = [
      path('',views.index,name='index'),
      path('mostrar',views.mostrar_Proyecto,name='mostrar_Proyecto'),
      
]