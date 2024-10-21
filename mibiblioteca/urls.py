from django.urls import path 
from . import views

app_name='mibiblioteca'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mostrar_usuarios', views.usuarios, name='mostrar_usuarios'),
    path('mostrar_libros', views.libros, name='mostrar_libros'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('editar_libros/<int:id>/', views.editar_libro, name='editar_libros'),
    path('crear_libros/', views.crear_libros, name='crear_libros'),
    path('eliminar_usuarios/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('eliminar_libros/<int:id>/', views.eliminar_libros, name='eliminar_libros'),
    path('editar_usuarios/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('buscar_libros/', views.buscar_libros, name='buscar_libros'),
]