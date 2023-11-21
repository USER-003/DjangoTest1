from django.shortcuts import render
from .models import Medico, Paciente
from .formularios import add_medico as fm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "index.html")

def database(request):
    medicos = Medico.objects.all()
    return render(request, "database.html", {"medicos":medicos})

def add_med(request):
    if request.method == "POST":
        formulario = fm.Add_medic(request.POST)
        if formulario.is_valid():
            nuevoreg = Medico()
            nuevoreg.nombre = formulario.data["nombre"]
            nuevoreg.apellido = formulario.data["apellido"]
            nuevoreg.especialidad = formulario.data["especialidad"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.Add_medic()
        return render(request, "form.html", {"form":formulario})