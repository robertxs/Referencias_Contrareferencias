from django.db import models
from django.core.validators import MaxValueValidator
from medico.models import *
from 

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
    medico_triaje = models.ForeignKey(Medico,
                                  on_delete=models.CASCADE)

class Historia(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)







