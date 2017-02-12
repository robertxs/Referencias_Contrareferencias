from django.db import models
from django.core.validators import MaxValueValidator
from administrador.models import *
from medico.models import *

class Paciente(models.Model):
    ESTADOS_CIVILES = (
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Viudo', 'Viudo'),
        ('Divorciado','Divorciado')
    )

    cedula = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)
    edad = models.IntegerField()
    tipo_sanguineo = models.CharField(max_length=20)
    alergias = models.CharField(max_length=100)
    adicciones = models.CharField(max_length=100)
    antecedentes_familiares = models.TextField()

class Historiadetriaje(models.Model):
    paciente = models.ForeignKey(Paciente,
                                  on_delete=models.CASCADE)
    medico_triaje = models.ForeignKey('medico.Medico',
                                  on_delete=models.CASCADE)

class Historia(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey('medico.Medico',
                               on_delete=models.CASCADE)
    especialidad = models.ForeignKey('medico.Especialidad',
                                     on_delete=models.CASCADE)







