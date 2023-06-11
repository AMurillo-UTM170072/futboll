from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from .forms import Liguilla,Equipos
from django.contrib.auth.decorators import login_required
from .models import Torneo
import os 
cardItem = [
    {'Nombre':'Alta de jugador',"url":"https://www.playerone.vg/wp-content/uploads/2021/05/ReZero-kara-Hajimeru-Isekai-Seikatsu-Hyouketsu-no-Kizuna-finaliza-e1622492984100.jpg","path":"infoJugadores"},
    {'Nombre':'Equipos',"url":"https://www.playerone.vg/wp-content/uploads/2021/05/ReZero-kara-Hajimeru-Isekai-Seikatsu-Hyouketsu-no-Kizuna-finaliza-e1622492984100.jpg","path":"equipoAlta"},
    {'Nombre':'Torneo',"url":"https://www.playerone.vg/wp-content/uploads/2021/05/ReZero-kara-Hajimeru-Isekai-Seikatsu-Hyouketsu-no-Kizuna-finaliza-e1622492984100.jpg","path":"directivoTorneo"},
    {'Nombre':'Arbitros',"url":"https://www.playerone.vg/wp-content/uploads/2021/05/ReZero-kara-Hajimeru-Isekai-Seikatsu-Hyouketsu-no-Kizuna-finaliza-e1622492984100.jpg","path":"infoJugadores"}
]
# Create your views here.import os
def inicio(resquest):
    return HttpResponse("<h1>Liga de futboll</h1>")

@login_required(login_url='accounts/')
def index (request):
    context = {'foo': 'bar'}
    return render(None, 'base.html', context)
def adminJournament(request):
    return render(request,'pages/adminHome/homeAdmin.html',{'dict':cardItem})
def getJournament (request):
    tournament = Torneo.objects.all()
    return render(request,'pages/adminHome/adminTableTorneos.html',{'tournament':tournament} )
def navegarOtro(request):
    return render('pages/adminHome/homeAdmin.html',{'dict':cardItem})
def jugadores (request):
    return render (request,'pages/jugadores/jugadores.html')
def infoJugadores (request):
    return render (request,'pages/jugadores/tableInfoJugadores.html')
def infoEquipo (request):
    return render (request,'pages/Equipos/tableInfoEquipos.html')
def altaEquipo (request):
    formularioEquipo  =  Equipos(request.POST or None)
    if formularioEquipo.is_valid():
        formularioEquipo.save()
    return render (request,'pages/Equipos/insertTeams.html',{"formulario":formularioEquipo})
def alta (request):
    return render (request,'pages/jugadores/tableInfoJugadores.html')
def altaTorneo(request):
    formulario = Liguilla(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    return render(request,"pages/torneoForm/formTemplate.html",{"formulario":formulario})
def altaJugador(request):
    return render(request,"pages/jugadores/jugadoresAlta.html")