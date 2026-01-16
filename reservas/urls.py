from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('reservar/', views.reservar_sala, name='reservar_sala'),
    path('minhas-reservas/', views.minhas_reservas, name='minhas_reservas'),
    path('cancelar-reserva/<int:pk>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('cadastrar-sala/', views.cadastrar_sala, name='cadastrar_sala'),
    path('editar-reserva/<int:pk>/', views.editar_reserva, name='editar_reserva'),
    path('gestao/', views.dashboard_admin, name='dashboard_admin'),
]
