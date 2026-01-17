from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Sala
from .models import Categoria
from django.utils import timezone

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
    
    def clean_data(self):
        data = self.cleaned_data.get('data')
        hoje = timezone.now().date()
        
        if data and data < hoje:
            raise forms.ValidationError('Não é possível reservar uma sala em uma data passada. Por favor, selecione hoje ou uma data futura.')
        
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fim = cleaned_data.get('hora_fim')
        
        # Validar que hora_fim é maior que hora_inicio
        if hora_inicio and hora_fim:
            if hora_fim <= hora_inicio:
                raise forms.ValidationError('O horário de término deve ser posterior ao horário de início.')
        
        # Validar que não é possível reservar em horário passado
        if data and hora_inicio:
            from django.utils.timezone import localtime
            agora = localtime(timezone.now())
            hoje = agora.date()
            hora_atual = agora.time()
            
            # Se a data é hoje, verificar se o horário já passou
            if data == hoje and hora_inicio <= hora_atual:
                raise forms.ValidationError('Não é possível reservar uma sala em um horário que já passou. Por favor, selecione um horário futuro.')
        
        return cleaned_data


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