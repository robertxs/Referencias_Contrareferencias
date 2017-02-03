from django.db import models
from django.core.validators import MaxValueValidator
from medico.models import *


class Paciente(models.Model):
    ESTADOS_CIVILES = (
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
    )
    cedula = models.IntegerField(primary_key=True,
                                 validators=[MaxValueValidator(99999999)])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=70)
    estado_civil = models.CharField(max_length=7, choices=ESTADOS_CIVILES)
    ocupacion = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField()


class Historiadetriaje(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico_triaje = models.ForeignKey(Medico,
                                      on_delete=models.CASCADE)


class Historia(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)
