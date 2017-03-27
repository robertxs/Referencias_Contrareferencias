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
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=70, blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    estado_civil = models.CharField(max_length=7, choices=ESTADOS_CIVILES, blank=True, null=True)
    ocupacion = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=70, blank=True, null=True)
    telefono = models.CharField(max_length=13, blank=True, null=True)
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)


    def __str__(self):
        return str(self.cedula) + "  " + self.first_name + " " + self.last_name


class Historiadetriaje(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico_triaje = models.ForeignKey('medico.Medico',
                                      on_delete=models.CASCADE)
    antecedentes_personales = models.CharField(max_length=500)
    antecedentes_familiares = models.CharField(max_length=500)
    motivo_consulta = models.CharField(max_length=200)
    enfermedad_actual = models.CharField(max_length=200)
    peso = models.DecimalField(max_digits=5,decimal_places=2)
    talla = models.DecimalField(max_digits=5,decimal_places=2)
    signos_vitales = models.CharField(max_length=200)
    piel = models.CharField(max_length=200)
    ojos = models.CharField(max_length=200)
    fosas_nasales = models.CharField(max_length=200)
    conductos_auditivos = models.CharField(max_length=200)
    cavidad_oral = models.CharField(max_length=200)
    cuello = models.CharField(max_length=200)
    columna = models.CharField(max_length=200)
    torax = models.CharField(max_length=200)
    abdomen = models.CharField(max_length=200)
    extremidades = models.CharField(max_length=200)
    genitales = models.CharField(max_length=200)

class Historia(models.Model):
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey('medico.Medico',
                               on_delete=models.CASCADE)
    especialidad = models.ForeignKey('medico.Especialidad',
                                     on_delete=models.CASCADE)
