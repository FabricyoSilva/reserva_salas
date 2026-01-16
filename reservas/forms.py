from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Sala


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

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('email', 'username') # O Django ainda pede username, mas focaremos no email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicando Tailwind e removendo textos de ajuda chatos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full p-2 border rounded-lg focus:ring-green-500'})
            field.help_text = '' 

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade', 'localizacao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
            'capacidade': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
            'localizacao': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
        }