from django import forms
from .models import Reserva, Comentario

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['entradas_reservadas']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']