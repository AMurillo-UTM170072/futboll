from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path (r'^juagadores/$',views.jugadores ,name='jugadores'),
    path (r'^jugadores/infoJugador/$',views.infoJugadores ,name='infoJugadores'),
]
''