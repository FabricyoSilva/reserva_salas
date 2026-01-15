from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['sala', 'data', 'hora_inicio', 'hora_fim']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border rounded'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full p-2 border rounded'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full p-2 border rounded'}),
            'sala': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        }