from django.http import HttpResponse
from django.template import loader # Usa esto en lugar de loader y HttpResponse
from programas.models import Programa

def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template('lista_programas.html')
    context = {
        'lista_programas': lista_programas,
        'total_programas': lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
