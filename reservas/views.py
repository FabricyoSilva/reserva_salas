from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sala
from .forms import ReservaForm 

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