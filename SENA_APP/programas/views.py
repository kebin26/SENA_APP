from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Programa
from .forms import ProgramaForm
from django.views.generic import FormView
from django.contrib import messages



class ProgramaListView(ListView):
    model = Programa
    template_name = 'lista_programas.html'
    context_object_name = 'programas'
    paginate_by = 10


class ProgramaDetailView(DetailView):
    model = Programa
    template_name = 'detalle_programa.html'
    context_object_name = 'programa'


# VISTA BASADA EN FUNCION DEL FORMULARIO DE PROGRAMA
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProgramaForm
from .models import Programa

def crear_programa(request):
    """Vista para crear un nuevo programa"""
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            try:
                programa = form.save()
                messages.success(
                    request, 
                    f'El Programa {programa.nombre} ha sido registrado exitosamente.'
                )
                return redirect('lista_programas')  # Cambia por tu URL de lista
            except Exception as e:
                messages.error(request, f'Error al guardar el programa: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
            # Para depuración, imprime los errores
            print("Errores del formulario:", form.errors)
    else:
        form = ProgramaForm()

    return render(request, 'crear_programas.html', {
        'form': form,
        'titulo': 'Registrar Nuevo Programa'
    })

# class ProgramaUpdateView(UpdateView):
#     model = Programa
#     form_class = ProgramaForm
#     template_name = 'editar_programa.html'
#     success_url = reverse_lazy('programas:lista_programas')

#     def form_valid(self, form):
#         return super().form_valid(form)


# class ProgramaDeleteView(DeleteView):
#     model = Programa
#     template_name = 'eliminar_programa.html'
#     success_url = reverse_lazy('programas:lista_programas')

#     def delete(self, request, *args, **kwargs):
#         return super().delete(request, *args, **kwargs)
