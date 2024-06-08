from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs de vistas normales
    # Crear la URL de la vista index
    path('',views.base, name='base'),       
    path('listar/', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear, name='crear'),
    path('listar_editar/', views.listar_editar, name='listar_editar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/', views.eliminar, name='eliminar_productos'),  
    path('eliminar/<int:id>/', views.eliminar_elemento, name='eliminar_producto'),
    path('exportar_csv/', views.exportar_csv, name='exportar_csv'),  
    path('importar_csv/', views.importar_csv, name='importar_csv'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)