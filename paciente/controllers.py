from administrador.models import *
from medico.models import *
from paciente.models import *
import datetime
import parsedatetime as pdt
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

def editar_paciente(user, nombre, apellido, sexo, ocupacion, fecha,
					lugar, estado_civil, telefono, direccion, email, foto):
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
		print("save")
		paciente.sexo = sexo
		print("sexo")
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
		print("fecha")
		paciente.lugar_nacimiento = lugar
		print("lug")
		paciente.ocupacion = ocupacion
		print("ocu")
		paciente.estado_civil = estado_civil
		print("estado")

		if (telefono == '') :
			pass
		else :
			paciente.telefono = telefono
		print("telf")
		paciente.direccion = direccion
		if foto != False :
			usuario.foto=foto
			usuario.fotosubida = True
		usuario.save()
		paciente.save()
		print("saveeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

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
		especialidad = Especialidad.objects.get(nombre_especialidad=especialidad)
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


def modificar_citas_paciente(cita_id, medico, institucion, descripcion,
                                  fecha,hora,especialidad, es_referido):
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
        institucion = Institucion.objects.get(id=institucion)
        cita.institucion = institucion
        especialidad = Especialidad.objects.get(nombre_especialidad=especialidad)
        cita.especialidad = especialidad
        cita.descripcion = descripcion
        cita.fecha = fecha
        cita.save()
        return True
    except:
        return False
