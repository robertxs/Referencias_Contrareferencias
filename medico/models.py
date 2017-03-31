from django.db import models
from administrador.models import *
from paciente.models import *
from django.core.validators import MaxValueValidator

class Medico(models.Model):
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

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return str(self.nombre_especialidad)

class Institucion(models.Model):
    TIPO = (
            ('Hospital', 'Hospital'),
            ('Clinica', 'Clinica'),
            ('Laboratorio', 'Laboratorio')
            )
    rif = models.CharField(max_length=12, blank=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=False)
    tipo = models.CharField(max_length=30, choices=TIPO, blank=False, default='')

    def __str__(self):
        return self.name


# Se contempla tener aqui donde trabaja el medico y la especialidad
class Medico_Especialidad(models.Model):
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion,
                                    on_delete= models.CASCADE)
    horario = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.horario)


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


class Medico_Citas(models.Model):
    HORARIOS = (
                ("6Am","6Am"),
                ("7Am","7Am"),
                ("8Am","8Am"),
                ("9Am","9Am"),
                ("10Am","10Am"),
                ("11Am","11Am"),
                ("12Pm","12Pm"),
                ("1Pm","1Pm"),
                ("2Pm","2Pm"),
                ("3Pm","3Pm"),
                ("4Pm","4Pm"),
                ("5Pm","5Pm")
                )
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion,
                                    on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500, blank=False)
    hora = models.CharField(max_length=5, choices=HORARIOS,blank=False)
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)
    revision = models.BooleanField(default=False)
    informe = models.BooleanField(default=False)
    es_referido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("paciente","medico","institucion","fecha")

class Medico_Revision(models.Model):
    cita = models.OneToOneField(Medico_Citas, on_delete=models.CASCADE, primary_key= True,)
    motivos = models.CharField(max_length=500, blank=False)
    sintomas = models.CharField(max_length=500, blank=False)
    presion_sanguinea_diastolica = models.IntegerField(blank=False, default=0)
    presion_sanguinea_sistolica =models.IntegerField(blank=False, default=0)
    temperatura =models.IntegerField(blank=False, default=0)
    frec_respiratoria =models.IntegerField(blank=False, default=0)
    frec_cardiaca =models.IntegerField(blank=False, default=0)
    otros = models.CharField(max_length=100, blank=True)


class Medico_Informe(models.Model):
    medico_Revision = models.ForeignKey(Medico_Revision,
                                        on_delete=models.CASCADE)
    desc_prediagnostico = models.TextField(max_length=100)
    recipe_medico = models.TextField()


class Referencia(models.Model):

    HORARIOS = (
                ("6Am","6Am"),
                ("7Am","7Am"),
                ("8Am","8Am"),
                ("9Am","9Am"),
                ("10Am","10Am"),
                ("11Am","11Am"),
                ("12Pm","12Pm"),
                ("1Pm","1Pm"),
                ("2Pm","2Pm"),
                ("3Pm","3Pm"),
                ("4Pm","4Pm"),
                ("5Pm","5Pm")
                )
    cita = models.ForeignKey(Medico_Citas,
                                        on_delete=models.CASCADE)

    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion,
                                    on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500, blank=False)
    hora = models.CharField(max_length=5, choices=HORARIOS,blank=False)
    especialidad = models.ForeignKey(Especialidad,
                                    on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='informes/')
