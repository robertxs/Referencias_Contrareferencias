from django.db import models
from administrador.models import *
from paciente.models import *
from medico.models import Laboratorio
from django.core.validators import MaxValueValidator

class Bioanalista(models.Model):
    cedula = models.IntegerField(primary_key=True,
                                 validators=[MaxValueValidator(99999999)])
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cedula) + " " + self.first_name + " " + self.last_name
        
class BioanalistaEnLab(models.Model):
	bioanalista = models.ForeignKey(Bioanalista, on_delete = models.CASCADE)
	laboratorio = models.ForeignKey(Laboratorio, on_delete = models.CASCADE)
	
	class Meta:
		unique_together = ('bioanalista', 'laboratorio')
