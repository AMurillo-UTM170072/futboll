from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('jugadores',views.jugadores ,name='jugadores'),
    path ('infoJugador',views.infoJugadores ,name='infoJugadores'),
]
''