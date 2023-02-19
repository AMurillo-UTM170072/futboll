from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('jugadores',views.jugadores ,name='jugadores'),
    path ('directivo',views.adminJournament  ,name='adminHome'),
    path ('directivo/Torneos',views.getJournament ,name='directivoTorneo'),
    path ('jugadores/infoJugador',views.infoJugadores ,name='infoJugadores'),
    path ('directivo/torneoAlta',views.altaTorneo ,name='altaTorneo'),
    path ('directivo/torneoAlta',views.altaTorneo,name="altaTorneo")
]