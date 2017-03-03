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
        return str(self.cedula) + "  " + self.first_name + " " + self.last_name

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(primary_key=True, max_length=30)

    def __str__(self):
        return str(self.nombre_especialidad)

class Institucion(models.Model):
    rif = models.CharField(max_length=10, primary_key = True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return str(self.rif) + "  " + self.name


# Se contempla tener aqui donde trabaja el medico y la especialidad
class Medico_Especialidad(models.Model):
    DISPONIBILIDAD = (
                    ('Si', 'Si'),
                    ('No', 'No')
                    )
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion,
                                    on_delete= models.CASCADE)
    horario = models.DateField()
    disponibilidad = models.CharField(max_length=2, choices=DISPONIBILIDAD, blank=False, null=False )


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
    paciente = models.ForeignKey(Paciente,
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion,
                                    on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500, blank=False)
    revision = models.BooleanField(default=False)
    informe = models.BooleanField(default=False)
    # especialidad = models.ForeignKey(Medico_Especialidad,
    #                                 on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("paciente","medico","institucion","fecha")

class Medico_Revision(models.Model):
    cita = models.OneToOneField(Medico_Citas, on_delete=models.CASCADE, primary_key= True,)
    motivos = models.CharField(max_length=500, blank=False)
    sintomas = models.CharField(max_length=500, blank=False)
    presion_sanguinea = models.CharField(max_length=30,blank=False)
    temperatura = models.CharField(max_length=500, blank = False)
    frec_respiratoria = models.CharField(max_length=500, blank = False)
    frec_cardiaca = models.CharField(max_length=50, blank = False)
    otros = models.CharField(max_length=50, blank=True)


class Medico_Informe(models.Model):
    medico_Revision = models.ForeignKey(Medico_Revision,
                                        on_delete=models.CASCADE)
    desc_prediagnostico = models.TextField(max_length=100)

class Medico_Diagnostico(models.Model):
    cita = models.ForeignKey(Medico_Citas,
                              on_delete=models.CASCADE)
    conclusiones = models.TextField()
    recipe_medico = models.TextField()

class Emergencia(models.Model):
    paciente = models.ForeignKey(Paciente,
                                        on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                                        on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion,
                                        on_delete=models.CASCADE)
    fecha_entrada = models.DateField()

    hora_entrada = models.DateTimeField()

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('paciente','medico','institucion')

class Referencia(models.Model):
  informe = models.ForeignKey(Medico_Informe,
                              on_delete=models.CASCADE)
  medico_referido = models.ForeignKey(Medico,
                                    on_delete=models.CASCADE)
  fecha_referencia = models.DateField()
  hora_referencia = models.DateTimeField()
