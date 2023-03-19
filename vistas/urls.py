from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('jugadores',views.jugadores ,name='jugadores'),
    path ('equipo',views.infoEquipo ,name='equipoAlta'),
    path ('directivo',views.adminJournament  ,name='adminHome'),
    path ('directivo/Torneos',views.getJournament ,name='directivoTorneo'),
    path ('jugadores/infoJugador',views.infoJugadores ,name='infoJugadores'),
    path ('directivo/equipoAlta',views.altaEquipo ,name='altaEquipo'),
    path ('directivo/torneoAlta',views.altaTorneo ,name='altaTorneo'),
    path ('jugadores/jugadorAlta',views.altaJugador,name="altaJugador")
]