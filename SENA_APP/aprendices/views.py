from django.shortcuts import render
from .models import Aprendiz

def inicio(request):
    return render(request, "inicio.html")

def aprendices(request):
    filtro = request.GET.get("buscar" )
    if filtro:
        lista = Aprendiz.objects.filter(nombre__icontains = filtro) 
        Aprendiz.objects.filter(apellido__icontains = filtro)
        
    else: 
        lista = Aprendiz.objects.all().values()
    return render(request, "lista_aprendices.html", {"aprendices": lista})

# Create your views here.
