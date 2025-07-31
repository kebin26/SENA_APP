from django.shortcuts import render
from django.http import HttpResponse
from .models import Aprendiz

def aprendices(request):
    filtro = request.GET.get('buscar')
    if filtro:
        lista = Aprendiz.objects.filter(nombre_icontains=filtro) | Aprendiz.objects.filter(apellido_icontains=filtro)
    else:
        lista = Aprendiz.objects.all()
    return render(request, 'lista_aprendices.html', {'aprendices': lista})
def inicio(request):
    return render(request, 'inicio.html')
