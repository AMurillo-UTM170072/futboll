from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
import os 
# Create your views here.import os
def inicio(resquest):
    return HttpResponse("<h1>Liga de futboll</h1>")

def index (request):
    context = {'foo': 'bar'}
    return render(None, 'base.html', context)
def admin(request):
    cardItem = [
        {'Nombre':'Alta de jugador'},
        {'Nombre':'Equipos'},
        {'Nombre':'Torneo'},
        {'Nombre':'Arbitros'}
    ]
    return render(request,'pages/adminHome/homeAdmin.html',{'dict':cardItem})

def jugadores (request):
    return render (request,'pages/jugadores/jugadores.html')
def infoJugadores (request):
    return render (request,'pages/jugadores/tableInfoJugadores.html')