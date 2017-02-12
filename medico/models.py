from django.db import models
from administrador.models import *
from paciente.models import *
from django.core.validators import MaxValueValidator

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(primary_key=True, max_length=30)

class Institucion(models.Model):
    rif = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=False)
    telefono = models.CharField(max_length=15)

class Medico(models.Model):
    #ESTADOS_CIVILES = (
    #    ('Soltero', 'Soltero'),
    #    ('Casado', 'Casado'),
    #    ('Viudo', 'Viudo'),
    #    ('Divorciado','Divorciado')
    #)    
    cedula = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)
    # especialidad = models.ForeignKey(Especialidad,
    #                                     on_delete=models.CASCADE)             
    centro_medico = models.ForeignKey(Institucion,
                                        on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    #fecha_nacimiento = models.DateField()
    #sexo = models.CharField(max_length=10)
    #estado_civil = models.CharField(max_length=15, choices=ESTADOS_CIVILES)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    # usuario = models.ForeignKey(Usuario,
    #                             on_delete=models.CASCADE)

class Medico_Especialidad(models.Model):
    especialidad = models.ForeignKey(Especialidad,
                                     on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)

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

class Cita(models.Model):
    cedula_paciente = models.ForeignKey(Paciente,
                                        on_delete=models.CASCADE)
    cedula_medico = models.ForeignKey(Medico,
                                        on_delete=models.CASCADE)
    fecha = models.DateField()
    rif_centro_medico = models.ForeignKey(Institucion,
                                        on_delete=models.CASCADE)
    hora = models.DateTimeField()
    # revision = models.ForeignKey('RevisionMedico',
    #                                 on_delete=models.CASCADE)
    # informe = models.ForeignKey('InformeMedico',
    #                                 on_delete=models.CASCADE)
    # diagnostico = models.ForeignKey('Diagnostico',
    #                                 on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad,
                                    on_delete=models.CASCADE)

class RevisionMedico(models.Model):
    cita_id = models.ForeignKey(Cita,
                              on_delete=models.CASCADE)
    motivos = models.CharField(max_length=500)
    sintomas = models.TextField()
    presion_sanguinea = models.CharField(max_length=30)
    temperatura = models.CharField(max_length=50)
    frec_respiratoria = models.CharField(max_length=50)
    frec_cardiaca = models.CharField(max_length=50)
    otros = models.TextField()

class InformeMedico(models.Model):
    cita_id = models.ForeignKey(Cita,
                              on_delete=models.CASCADE)
    sintomas_signos = models.TextField()
    desc_prediagnostico = models.TextField()

class Diagnostico(models.Model):
    cita_id = models.ForeignKey(Cita,
                              on_delete=models.CASCADE)
    conclusiones = models.TextField()
    recipe_medico = models.TextField()

class Emergencia(models.Model):
    cedula_paciente = models.ForeignKey(Paciente,
                                        on_delete=models.CASCADE)
    cedula_medico = models.ForeignKey(Medico,
                                        on_delete=models.CASCADE)
    rif_centro_emerg = models.ForeignKey(Institucion,
                                        on_delete=models.CASCADE)
    fecha_entrada = models.DateField()

    hora_entrada = models.DateTimeField()

class CentroMedico(models.Model):
    rif = models.ForeignKey(Institucion,
                            on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad,
                                        on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico,
                                on_delete=models.CASCADE)
class Laboratorio(models.Model):
    rif = models.ForeignKey(Institucion,
                            on_delete=models.CASCADE)
    estudios = models.CharField(max_length=100)
    horario_atencion = models.CharField(max_length=50)

class Horarios(models.Model):
    DISPONIBILIDAD = (
        ('Si', 'Si'),
        ('No', 'No')
    )    
    cedula_medico_tratante = models.ForeignKey(Medico,
                                                on_delete=models.CASCADE)
    rif = models.ForeignKey(Institucion,
                                on_delete=models.CASCADE)
    hora_cita = models.DateTimeField()
    disponible = models.CharField(max_length=2, choices=DISPONIBILIDAD) 

class ReferenciaMedico(models.Model):
  cita_id = models.ForeignKey(Cita,
                              on_delete=models.CASCADE)
  # cedula_paciente = models.ForeignKey(Paciente,
  #                                     on_delete=models.CASCADE)
  # cedula_medico_tratante = models.ForeignKey(Medico, related_name= 'ci_medico_referido',
  #                                             on_delete=models.CASCADE)
  cedula_medico_referido = models.ForeignKey(Medico, 
                                              on_delete=models.CASCADE)
  fecha_referencia = models.DateField()
  hora_referencia = models.DateTimeField()


class ReferenciaLaboratorio(models.Model):
  cita_id = models.ForeignKey(Cita,
                              on_delete=models.CASCADE)
  # cedula_paciente = models.ForeignKey(Paciente,
  #                                     on_delete=models.CASCADE)
  # cedula_medico_tratante = models.ForeignKey(Medico,
  #                                             on_delete=models.CASCADE)
  examenes_estudios = models.TextField()