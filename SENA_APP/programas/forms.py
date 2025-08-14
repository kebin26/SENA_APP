from django import forms
from .models import Programa

class ProgramaForm(forms.Form):
    codigo = forms.CharField(max_length=20, label="Código", help_text="Ingrese el código único del programa.")
    nombre = forms.CharField(max_length=200, label="Nombre", help_text="Ingrese el nombre del programa.")
    version = forms.IntegerField(min_value=1, label="Versión", help_text="Ingrese la versión del programa.")
    nivel_formacion = forms.ChoiceField(choices=Programa.NIVEL_FORMACION_CHOICES, label="Nivel de Formación", help_text="Seleccione el nivel de formación del programa.")
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, label="Estado", help_text="Seleccione el estado del programa.")
    duracion_horas = forms.IntegerField(min_value=1, label="Duración (horas)", help_text="Ingrese la duración del programa en horas.")
    area_formacion = forms.CharField(max_length=100, label="Área de Formación", help_text="Ingrese el área de formación del programa.")
    fecha_inicio = forms.DateField(label="Fecha de Inicio", help_text="Ingrese la fecha de inicio del programa.")
    fecha_fin = forms.DateField(label="Fecha de Finalización", help_text="Ingrese la fecha de finalización del programa.")
    centro_formacion = forms.CharField(max_length=100, label="Centro de Formación", help_text="Ingrese el centro de formación donde se imparte el programa.")
    descripcion = forms.CharField(widget=forms.Textarea, required=False, label="Descripción", help_text="Ingrese una descripción del programa.")

    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nombre = cleaned_data.get('nombre')
        if not codigo or not nombre:
            raise forms.ValidationError("El código y el nombre del programa son obligatorios.")
        return cleaned_data

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if Programa.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("Ya existe un programa con este código.")
        return codigo

    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data['fecha_inicio']
        fecha_fin = self.cleaned_data.get('fecha_fin')
        if fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de finalización.")
        return fecha_inicio

    def save(self):
        """Método para guardar el programa en la base de datos"""
        try:
            programa = Programa.objects.create(
                codigo=self.cleaned_data['codigo'],
                nombre=self.cleaned_data['nombre'],
                version=self.cleaned_data['version'],
                nivel_formacion=self.cleaned_data['nivel_formacion'],
                estado=self.cleaned_data['estado'],
                duracion_horas=self.cleaned_data['duracion_horas'],
                area_formacion=self.cleaned_data['area_formacion'],
                fecha_inicio=self.cleaned_data['fecha_inicio'],
                fecha_fin=self.cleaned_data['fecha_fin'],
                centro_formacion=self.cleaned_data['centro_formacion'],
                descripcion=self.cleaned_data.get('descripcion', '')
            )
            return programa
        except Exception as e:
            raise forms.ValidationError(f"Error al crear el programa: {str(e)}")
