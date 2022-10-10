from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(resquest):
    return HttpResponse("<h1>Liga de futboll</h1>")