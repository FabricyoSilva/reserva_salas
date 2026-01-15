from django.shortcuts import render
from .models import Sala

def home(request):
    salas = Sala.objects.all()
    return render(request, 'reservas/home.html', {'salas': salas})