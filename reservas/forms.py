from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Sala

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ('email', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full p-2 border rounded-lg'})
            field.help_text = ''
            
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


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nome', 'capacidade', 'localizacao', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
            'capacidade': forms.NumberInput(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
            'localizacao': forms.TextInput(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
            'categoria': forms.Select(attrs={'class': 'w-full p-3 border rounded-lg focus:ring-blue-500'}),
        }