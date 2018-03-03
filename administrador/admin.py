from django.contrib import admin
from administrador.models import *
from medico.models import *
from paciente.models import *
from bioanalista.models import *

# Register your models here.
admin.site.register(Medico)
admin.site.register(Medico_Estudios)
admin.site.register(Medico_Logros)
admin.site.register(Institucion)
admin.site.register(Medico_Publicaciones)
admin.site.register(Paciente)
admin.site.register(Usuario)
admin.site.register(Historiadetriaje)
admin.site.register(Medico_Especialidad)
admin.site.register(Especialidad)
admin.site.register(Laboratorio)
admin.site.register(Bioanalista)
admin.site.register(Tipoexamen)