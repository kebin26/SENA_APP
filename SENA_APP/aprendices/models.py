from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=50)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=50)
    programa = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"



# Create your models here.
