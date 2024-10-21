from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.
def inicio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        password = request.POST.get('password')
        
    
        usuario=Usuarios.objects.get(nombre=nombre,password = password)
        return redirect('mibiblioteca:mostrar_usuarios')
    else:
        form = Usuariologin()
    return render(request,'inicio.html', {'form':form})


def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'crudusuarios.html', {'usuarios': usuarios})

def libros(request):
    libros = Libros.objects.all()
    return render(request, 'crudlibros.html', {'libros': libros})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, id=id)  
    usuario.delete()  
    return redirect('mibiblioteca:mostrar_usuarios')
def crear_usuario(request):
    if request.method == 'POST':
        form = Usuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mibiblioteca:mostrar_usuarios')  # Redirect to a success page after form submission
    else:
        form = Usuario()
    return render(request, 'crearusuario.html', {'form': form})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuarios, id=id)

    if request.method == 'POST':
        form = Usuario(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('mibiblioteca:mostrar_usuarios')
    else:
        form = Usuario(instance=usuario) 

    return render(request, 'editar_usuario.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libros, id=id)

    if request.method == 'POST':
        form = crearlibro(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('mibiblioteca:mostrar_libros')
    else:
        form = crearlibro(instance=libro) 

    return render(request, 'editar_libro.html', {'form': form})

def crear_libros(request):
    if request.method == 'POST':
        form = crearlibro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mibiblioteca:mostrar_libros')  # Redirect after saving
    else:
        form = crearlibro()
    return render(request, 'crear_libros.html', {'form': form})

def eliminar_libros(request, id):
    libro = get_object_or_404(Libros, id=id)  
    libro.delete()  
    return redirect('mibiblioteca:mostrar_libros')

def buscar_libros(request):
    query = request.GET.get('query', '')
    libros = Libros.objects.filter(titulo__icontains=query) if query else None
    return render(request, 'busqueda.html', {'libros': libros})