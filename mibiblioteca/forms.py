from django import forms
from .models import *

estado = (
    ("1", "Vivo"),
    ("2", 'Muerto')
)

class Usuariologin(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre','password']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'contraseña'})
        } 
class Usuario(forms.ModelForm):
    id_rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}), label='Rol')
    estado = forms.ChoiceField(choices=estado, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta: 
        model = Usuarios
        fields = ['nombre', 'correo', 'password', 'id_rol', 'estado']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'correo' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electronico'}),
            'password' : forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'contraseña'}),
            'estado': forms.ChoiceField(choices = estado)
        }

class crearlibro(forms.ModelForm):
    id_autor = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Autor'
    )
    id_editorial = forms.ModelChoiceField(
        queryset=Editorial.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Editorial'
    )
    idioma = forms.ModelChoiceField(
        queryset=Idioma.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Idioma'
    )
    estado = forms.ChoiceField(
        choices=estado, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Libros
        fields = ['titulo', 'fpublicacion', 'stock', 'nro_paginas', 'id_autor', 'id_editorial', 'idioma', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'fpublicacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Publicacion'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Stock'}),
            'nro_paginas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el Numero de Paginas'}),
        }