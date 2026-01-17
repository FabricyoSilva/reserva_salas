from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Sala
from .models import Categoria

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ('email', 'username')
        labels = {
            'email': 'Email',
            'username': 'Nome de usuário',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full p-2 border rounded-lg'})
            field.help_text = ''
        
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de senha'
            
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['sala', 'data', 'hora_inicio', 'hora_fim']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border rounded'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full p-2 border rounded'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full p-2 border rounded'}),
            'sala': forms.Select(attrs={'class': 'w-full p-2 border rounded appearance-none'}),
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

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none',
                'placeholder': 'Ex: Sala de Reunião, Laboratório...'
            }),
        }