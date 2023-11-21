from django.shortcuts import render
from .models import Medico, Paciente
from .formularios import add_medico as fm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "index.html")

def database(request):
    medicos = Medico.objects.all()
    return render(request, "database.html", {"medicos":medicos})