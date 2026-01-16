from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sala
from .forms import ReservaForm 
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import SalaForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
@login_required
def home(request):
    salas = Sala.objects.all()
    return render(request, 'reservas/home.html', {'salas': salas})

@login_required
def reservar_sala(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user 
            reserva.save()
            return redirect('home')
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/reservar.html', {'form': form})
@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'reservas/minhas_reservas.html', {'reservas': reservas})

@login_required
def cancelar_reserva(request, pk):
    # Garante que o usuário só consiga deletar as PRÓPRIAS reservas
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        reserva.delete()
        return redirect('minhas_reservas')
    
    return render(request, 'reservas/confirmar_cancelamento.html', {'reserva': reserva})

@staff_member_required
def cadastrar_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SalaForm()
    return render(request, 'reservas/cadastrar_sala.html', {'form': form})