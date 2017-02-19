from administrador.models import *
from medico.models import *
from paciente.models import *
import datetime
import parsedatetime as pdt
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


# def agragar_cita(user_pk, medico_ci, institucion, fecha, descripcion):
#
#     try:
#         paciente = Paciente.objects.get()
