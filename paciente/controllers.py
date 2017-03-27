from administrador.models import *
from medico.models import *
from paciente.models import *
import datetime
import parsedatetime as pdt
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

def editar_paciente(user, nombre, apellido, sexo, ocupacion, fecha, 
					lugar, estado_civil, telefono, direccion, email):
	try:
		usuario = Usuario.objects.get(user=user)
		user = User.objects.get(pk=usuario.user.pk)
		paciente = Paciente.objects.get(usuario=usuario)
		paciente.first_name = nombre
		user.first_name = nombre
		paciente.last_name = apellido
		user.last_name = apellido
		user.email = email
		user.save()
		paciente.sexo = sexo
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

		paciente.fecha_nacimiento = fecha
		paciente.lugar_nacimiento = lugar
		paciente.ocupacion = ocupacion
		paciente.estado_civil = estado_civil
		
		if (telefono == '') :
			pass			
		else :
			paciente.telefono = telefono

		paciente.direccion = direccion
		paciente.save()
		
		return True

	except:
		return False


def agregar_citas_paciente(user_pk, medico, institucion, descripcion, fecha, hora, especialidad, es_referido):
	try:
		user = User.objects.get(pk=user_pk)
		usuario = Usuario.objects.get(user=user)
		paciente = Paciente.objects.get(usuario=usuario)
		medico = Medico.objects.get(cedula=medico)
		institucion = Institucion.objects.get(id=institucion)
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
                            fecha=fecha,
                            hora=hora,
                            especialidad=especialidad,
                            es_referido = es_referido)
		cita.save()
		return True
	except:
		return False


def modificar_citas_paciente(cita_id, medico, descripcion, fecha, hora):
    try:
        cita = Medico_Citas.objects.get(
            pk=cita_id)
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
        medico = Medico.objects.get(cedula=medico)
        cita.medico = medico
        cita.hora = hora
        cita.descripcion = descripcion
        cita.fecha = fecha
        cita.save()
        return True
    except:
        return False
