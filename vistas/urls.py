from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('jugadores',views.jugadores ,name='jugadores'),
    path ('jugadores/infoJugador',views.infoJugadores ,name='infoJugadores'),
]