from administrador.models import *
from medico.models import *
from paciente.models import *
import datetime
import parsedatetime as pdt
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


def agregar_citas_paciente(user_pk, medico, institucion, descripcion, fecha):
    print("CONTROLADOR PACIENTE")
    try:
        user = User.objects.get(pk=user_pk)
        usuario = Usuario.objects.get(user=user)
        paciente = Paciente.objects.get(usuario=usuario)
        medico = Medico.objects.get(cedula=medico)
        institucion = Institucion.objects.get(rif=institucion)
        try:
            fecha = datetime.datetime.strptime(fecha,
                                               '%d-%m-%Y'
                                               ).strftime('%Y-%m-%d')
        except:
            if fecha is None:
                fecha = None
            else:
                cal = pdt.Calendar()
                now = datetime.datetime.now()
                fecha = cal.parseDT(fecha, now)[0]

        cita = Medico_Citas(paciente=paciente,
                            medico=medico,
                            institucion = institucion,
                            descripcion=descripcion,
                            fecha=fecha)
        cita.save()
        return True
    except:
        return False