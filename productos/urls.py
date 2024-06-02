from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    # Crear la URL de la vista index
    path('',views.base, name='base'),       
    path('listar/', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear, name='crear'),
    path('listar_editar/', views.listar_editar, name='listar_editar'),
    path('editar/<int:id>/', views.editar, name='editar'),
     path('eliminar/', views.eliminar, name='eliminar_productos'),  
    path('eliminar/<int:id>/', views.eliminar_elemento, name='eliminar_producto'),  
]