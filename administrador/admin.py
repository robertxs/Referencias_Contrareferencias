from django.contrib import admin
from . import models
from medico import models
from paciente import models

# Register your models here.

# Registro de Modelo Administrador.
admin.site.register(models.Usuario)
admin.site.register(models.Inbox)

# Registro de Modelo Medico.
admin.site.register(models.Especialidad)
admin.site.register(models.Medico)
admin.site.register(models.Medico_Especialidad)
admin.site.register(models.Institucion)
admin.site.register(models.Medico_Estudios)
admin.site.register(models.Medico_Habilidades)
admin.site.register(models.Medico_Experiencias)
admin.site.register(models.Medico_Logros)
admin.site.register(models.Medico_Publicaciones)
admin.site.register(models.Medico_Eventos)
admin.site.register(models.Cita)
admin.site.register(models.RevisionMedico)
admin.site.register(models.InformeMedico)
admin.site.register(models.Diagnostico)
admin.site.register(models.Emergencia)
admin.site.register(models.CentroMedico)
admin.site.register(models.Laboratorio)
admin.site.register(models.Horarios)

# Registro de Modelo Paciente.
admin.site.register(models.Paciente)
admin.site.register(models.Historiadetriaje)
admin.site.register(models.Historia)
admin.site.register(models.ReferenciaMedico)
admin.site.register(models.ReferenciaLaboratorio)