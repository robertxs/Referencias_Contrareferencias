from django.db import models
from administrador.models import *
from django.core.validators import MaxValueValidator


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(primary_key=True, max_length=30)


class Medico(models.Model):
    cedula = models.IntegerField(primary_key=True,
                                 validators=[MaxValueValidator(99999999)])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)


class Medico_Especialidad(models.Model):
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)


class Institucion(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=255, blank=False)


class Medico_Estudios(models.Model):
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500, blank=False)
    fecha_graduacion = models.DateField()
    descripcion = models.CharField(max_length=500, blank=False)
    institucion = models.CharField(max_length=500, blank=False)


class Medico_Habilidades(models.Model):
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500, blank=False)
    descripcion = models.CharField(max_length=500, blank=False)


class Medico_Experiencias(models.Model):
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500, blank=False)
    descripcion = models.CharField(max_length=500, blank=False)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    institucion = models.CharField(max_length=500, blank=False)


class Medico_Logros(models.Model):
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500, blank=False)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500, blank=False)


class Medico_Publicaciones(models.Model):
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, blank=False)
    autores = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=500, blank=False)
    revista = models.CharField(max_length=100, blank=False)
    numero = models.CharField(max_length=5, blank=False)
    volumen = models.CharField(max_length=5, blank=False)
    fecha = models.DateField()


class Medico_Eventos(models.Model):
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500, blank=False)
    descripcion = models.CharField(max_length=500, blank=False)
    institucion = models.CharField(max_length=500, blank=False)
    date = models.DateField()
