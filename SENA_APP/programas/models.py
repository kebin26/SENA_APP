from django.db import models

class Programa(models.Model):
    ESTADO_CHOICES = [
        ('ACT', 'Activo'),
        ('INA', 'Inactivo'),
        ('SUS', 'Suspendido'),
    ]

    NIVEL_FORMACION_CHOICES = [
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('ESP', 'Especialización'),
        ('PRE', 'Pregrado'),
        ('MAE', 'Maestría'),
        ('DOC', 'Doctorado'),
    ]
    
    area_formacion = models.CharField(max_length=100, default="Sin área")
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    version = models.PositiveIntegerField(default=1)
    nivel_formacion = models.CharField(max_length=3, choices=NIVEL_FORMACION_CHOICES, default='TEC')
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='ACT')
    duracion_horas = models.PositiveIntegerField()
    area_formacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    centro_formacion = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} (Versión {self.version})"

    def nombre_completo(self):
        return f"{self.codigo}: {self.nombre}"
