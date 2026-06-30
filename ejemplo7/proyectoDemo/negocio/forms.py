from negocio.models import Comment
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from negocio.models import Restaurante, Chef, Plato

class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'tipo_cocina', 'capacidad_meses']

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = ['nombres', 'anios_experiencia', 'especialidad_culinaria',
                  'restaurante']

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre_plato', 'descripcion', 'precio_plato',
                  'ingredientes_principales', 'chef']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control'}),
        }