from django.contrib import admin
# from . import models
from administrador.models import *
from medico.models import *
from paciente.models import *

# Register your models here.

# Registro de Modelo Administrador.
admin.site.register(Usuario)
admin.site.register(Inbox)

# Registro de Modelo Medico.
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Medico_Especialidad)
admin.site.register(Institucion)
admin.site.register(Medico_Estudios)
admin.site.register(Medico_Habilidades)
admin.site.register(Medico_Experiencias)
admin.site.register(Medico_Logros)
admin.site.register(Medico_Publicaciones)
admin.site.register(Medico_Eventos)
admin.site.register(Cita)
admin.site.register(RevisionMedico)
admin.site.register(InformeMedico)
admin.site.register(Diagnostico)
admin.site.register(Emergencia)
admin.site.register(CentroMedico)
admin.site.register(Laboratorio)
admin.site.register(Horarios)

# Registro de Modelo Paciente.
admin.site.register(Paciente)
admin.site.register(Historiadetriaje)
admin.site.register(Historia)
admin.site.register(ReferenciaMedico)
admin.site.register(ReferenciaLaboratorio)