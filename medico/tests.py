# -*- coding: utf-8 -*-
from django.test import TestCase
from datetime import datetime
from  medico.forms import*
from  medico.controllers import *
from  medico.models import *
from  paciente.models import *
from django.test.client import RequestFactory

#####################################################################
#                 			CONTROLADORES
#####################################################################

class MedicoTestCase(TestCase):

    def setUp(self):

    	self.factory = RequestFactory()

        User.objects.create(username = "medicos",password = "g4g4")
        medicos = User.objects.get(username = "medicos") 

        Usuario.objects.create(user = medicos,ci = "1111")
        medicos1 = Usuario.objects.get(ci = "1111")


        Medico.objects.create(cedula = 202020,first_name = "roberto",last_name = "rinaldi",
            fecha_nacimiento = "2015-02-15",sexo = "m",estado_civil = "s",telefono = "02125555",
            direccion = "dir", usuario = medicos1)
        medico = Medico.objects.get(cedula = 202020)

        User.objects.create(username = "paciente",password = "123")
        paciente = User.objects.get(username = "paciente")

        Usuario.objects.create(user = paciente,ci = "12345678")
        paciente1 = Usuario.objects.get(ci = "12345678")

        Paciente.objects.create(cedula = 12345678, first_name = "Cinthya", last_name = "Ramos",
                                usuario = paciente1)

        Institucion.objects.create(rif = 666555446, name = "Centro Medico La Trinidad",
                                    address = "La Trinidad")
        institucion = Institucion.objects.get(rif = 666555446)

        Institucion.objects.create(rif = 666555447, name = "La Arboleda",
                                    address = "Baruta")

        Especialidad.objects.create(nombre_especialidad = 'Cardiologia')

        Especialidad.objects.create(nombre_especialidad = 'Dermatologia')

	#####################################################################
	#                 			AGREGAR CITAS
	#####################################################################

	# Casos Malicia
    def test_agregar_citas_campos_vacios(self):
        medico = None
        paciente = None
        institucion = None
        descripcion = ''
        especialidad = None
        fecha = None
        hora = ''
        es_referido = None

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_campos_erroneos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 12345
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = 1234
        hora = 'Hola'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.rif,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha=fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

	# Casos Borde
    def test_agregar_citas_un_campo_lleno(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = ''
        institucion = ''
        descripcion = ''
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=user.pk,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_dos_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = ''
        descripcion = ''
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_tres_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = ''
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_cuatro_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_cinco_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = None
        hora = None
        es_referido = None

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_seis_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '23-04-2017'
        hora = None
        es_referido = None

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_siete_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '23-04-2017'
        hora = '7AM'
        es_referido = None

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_agregar_citas_campos_llenos(self):
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, True)

	#####################################################################
	#                 			MODIFICAR CITAS
	#####################################################################

	# Casos Malicia
    def test_modificar_citas_campos_vacios(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Modificar Cita
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
        paciente = None
        descripcion = None
        fecha = None
        hora = None

        value = modificar_citas(cita_id = cita.id, paciente = paciente,
        						descripcion = descripcion, fecha = fecha, hora = hora)

        self.assertIs(value,False)

    def test_modificar_citas_campos_erroneos(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Modificar Cita
        cita = Medico_Citas.objects.get(paciente = 12345678)
        descripcion = None
        fecha = 'Hola'

        value = modificar_citas(cita_id = cita.id, paciente = paciente.cedula,
        						descripcion = descripcion, fecha = fecha, hora = hora)

        self.assertIs(value,False)

	# Casos Bordes
    def test_modificar_citas_campo_descripcion(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Modificar Cita
        cita = Medico_Citas.objects.get(paciente = 12345678)
        descripcion = 'Cita Vieja'
        fecha = '28-03-2017'

        value = modificar_citas(cita_id = cita.id, paciente = paciente.cedula,
        						descripcion = descripcion, fecha = fecha, hora = hora)

        self.assertIs(value,True)

    def test_modificar_citas_campo_fecha(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Modificar Cita
        cita = Medico_Citas.objects.get(paciente = 12345678)
        fecha = '30-03-2017'

        value = modificar_citas(cita_id = cita.id, paciente = paciente.cedula,
        						descripcion = descripcion, fecha = fecha, hora = hora)

        self.assertIs(value,True)

    def test_modificar_citas_campo_hora(self):
        # Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Modificar Cita
        cita = Medico_Citas.objects.get(paciente = 12345678)
        hora = '11AM'

        value = modificar_citas(cita_id = cita.id, paciente = paciente.cedula,
                                descripcion = descripcion, fecha = fecha, hora = hora)

        self.assertIs(value,True)

    def test_modificar_citas_campos_llenos(self):
    	# Agregar Cita
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	paciente = Paciente.objects.get(cedula = 12345678)
    	institucion = Institucion.objects.get(rif = 666555446)
    	descripcion = 'Nueva Cita'
    	especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
    	fecha = '28-03-2017'
    	hora = '7AM'
    	es_referido = False

    	value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
    						descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
    						fecha= fecha,hora = hora, es_referido = es_referido)

    	# Modificar Cita
    	cita = Medico_Citas.objects.get(paciente = 12345678)
    	descripcion = 'Cita Vieja'
    	fecha = '30-03-2017'

    	value = modificar_citas(cita_id = cita.id, paciente = paciente.cedula,
    							descripcion = descripcion, fecha = fecha, hora = hora)

    	self.assertIs(value,True)

	#####################################################################
	#                 			AGREGAR CONSULTAS
	#####################################################################

	# Casos Malicia
    def test_agregar_consulta_campos_vacios(self):
    	especialidad = None
    	medico = None
    	institucion = None
    	hora = None

    	value = agregar_consultas(medico_id = medico, especialidad = especialidad,
    								institucion = institucion, hora = hora)

    	self.assertIs(value, False)

    def test_agregar_consulta_campos_erroneos(self):
    	especialidad = 5
    	medico = None
    	institucion = 666555447
    	hora = None

    	value = agregar_consultas(medico_id = medico, especialidad = especialidad,
    								institucion = institucion, hora = hora)

    	self.assertIs(value, False)

	# Casos Borde
    def test_agregar_consulta_campo_especialidad(self):
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = 'Dermatologia'
    	institucion = None
    	hora = None

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion, hora = hora)

    	self.assertIs(value, False)

    def test_agregar_consulta_campo_institucion(self):
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = None
    	institucion = 12345
    	hora = None

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion, hora = hora)

    	self.assertIs(value, False)

    def test_agregar_consulta_campos_llenos(self):
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = Especialidad.objects.get(nombre_especialidad = 'Dermatologia')
    	institucion = Institucion.objects.get(rif = 666555447)
    	hora = '8AM'

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion.pk, hora = hora)

    	self.assertIs(value, True)

	#####################################################################
	#                 			MODIFICAR CONSULTAS
	#####################################################################

	# Casos Malicia
    def test_modificar_consulta_campos_vacios(self):
    	# Agregar Consulta
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = Especialidad.objects.get(nombre_especialidad = 'Dermatologia')
    	institucion = Institucion.objects.get(rif = 666555447)
    	hora = '7AM'

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion.pk, hora = hora)

    	# Modificar Consulta
    	hora = None
    	consulta = Medico_Especialidad.objects.get(especialidad = 'Dermatologia')

    	value = modificar_consultas(consulta_id = consulta.pk, medico_id = user.pk,
                                    hora = hora)

    	self.assertIs(value, False)

    def test_modificar_consulta_campos_erroneos(self):
    	# Agregar Consulta
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = Especialidad.objects.get(nombre_especialidad = 'Dermatologia')
    	institucion = Institucion.objects.get(rif = 666555447)
    	hora = '7AM'

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion.pk, hora = hora)

    	# Modificar Consulta
    	hora = None
    	consulta = Medico_Especialidad.objects.get(especialidad = 'Dermatologia')

    	value = modificar_consultas(consulta_id = consulta.pk, medico_id = user.pk,
                                    hora = hora)

    	self.assertIs(value, False)

    # Casos Bordes

    def test_modificar_consulta_campo_hora(self):
    	# Agregar Consulta
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = Especialidad.objects.get(nombre_especialidad = 'Dermatologia')
    	institucion = Institucion.objects.get(rif = 666555447)
    	hora = '7AM'

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion.pk, hora = hora)

    	# Modificar Consulta
        hora = '12AM'
    	consulta = Medico_Especialidad.objects.get(especialidad = 'Dermatologia')

    	value = modificar_consultas(consulta_id = consulta.pk, medico_id = user.pk,
                                    hora = hora)

    	self.assertIs(value, True)


    def test_modificar_consulta_campos_llenos(self):
    	# Agregar Consulta
    	medico = Medico.objects.get(cedula=202020)
    	user = User.objects.get(username=medico.usuario.user)
    	especialidad = Especialidad.objects.get(nombre_especialidad = 'Dermatologia')
    	institucion = Institucion.objects.get(rif = 666555447)
    	hora = '7AM'

    	value = agregar_consultas(medico_id = user.pk, especialidad = especialidad,
    								institucion = institucion.pk, hora = hora)

    	# Modificar Consulta
    	hora = '5PM'

    	consulta = Medico_Especialidad.objects.get(especialidad = 'Dermatologia')

    	value = modificar_consultas(consulta_id = consulta.pk, medico_id = user.pk,
                                    hora = hora)

    	self.assertIs(value, True)

	####################################################################
	#                			COMENZAR REVISIÓN
	####################################################################

	# Casos Malicia
    def test_comenzar_revision_campos_vacios(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

    	# Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
    	motivos = None
    	sintomas = None
        presion_sanguinea_diastolica = None
        presion_sanguinea_sistolica = None
    	temperatura = None
    	frec_respiratoria = None
    	frec_cardiaca = None
    	otros = None

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	self.assertIs(value, False)

    def test_comenzar_revision_campos_erroneos(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, True)

    	# Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
    	motivos = None
    	sintomas = 1234
        presion_sanguinea_diastolica = None
        presion_sanguinea_sistolica = None
    	temperatura = 65
    	frec_respiratoria = None
    	frec_cardiaca = None
    	otros = None

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	self.assertIs(value, False)

    def test_comenzar_revision_campo_aleatorio_vacio(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

    	# Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
    	motivos = 'Dolor de Cabeza'
    	sintomas = 'Vomito'
        presion_sanguinea_diastolica = 60
        presion_sanguinea_sistolica = 49
    	temperatura = 32
    	frec_respiratoria = 100
    	frec_cardiaca = None
    	otros = 'Sin cita'

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	self.assertIs(value, False)

    # Casos Bordes

    def test_comenzar_revision_campo_otros_vacio(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

    	# Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
    	motivos = 'Dolor de Cabeza'
    	sintomas = 'Vomito'
        presion_sanguinea_diastolica = 60
        presion_sanguinea_sistolica = 49
    	temperatura = 32
    	frec_respiratoria = 40
    	frec_cardiaca = 20
    	otros = ''

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)


    	self.assertIs(value, True)

    def test_comenzar_revision_campo_otros_lleno(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

    	# Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
    	motivos = 'Dolor de Cabeza'
    	sintomas = 'Vomito'
        presion_sanguinea_diastolica = 60
        presion_sanguinea_sistolica = 49
    	temperatura = 32
    	frec_respiratoria = 15
    	frec_cardiaca = 20
    	otros = 'Sintomas'

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	self.assertIs(value, True)

	#####################################################################
	#                 			INFORME MÉDICO
	#####################################################################

	# Casos Malicia
    def test_informe_medico_campo_vacio(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
        motivos = 'Dolor de Cabeza'
        sintomas = 'Vomito'
        presion_sanguinea_diastolica = 60
        presion_sanguinea_sistolica = 49
        temperatura = 32
        frec_respiratoria = 15
        frec_cardiaca = 20
        otros = 'Sintomas'

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	# Informe Médico
    	revision = None
    	prediagnostico = None
        recipe_medico = None

    	value = informe_medico(revision_id = revision, prediagnostico = prediagnostico,
                                recipe = recipe_medico)

    	self.assertIs(value, False)

    # Casos Bordes
    def test_informe_medico_campos_prediagnostico_vacio(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
        motivos = 'Dolor de Cabeza'
        sintomas = 'Vomito'
        presion_sanguinea_diastolica = 60
        presion_sanguinea_sistolica = 49
        temperatura = 32
        frec_respiratoria = 15
        frec_cardiaca = 20
        otros = 'Sintomas'

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	# Informe Médico
    	revision = Medico_Revision.objects.get(motivos = 'Dolor de Cabeza')
    	prediagnostico = None
        recipe_medico = 'Tomar Pildoras de Tranquilidad'

        value = informe_medico(revision_id = revision.pk, prediagnostico = prediagnostico,
                                recipe = recipe_medico)
 
    	self.assertIs(value, False)

    def test_informe_medico_campos_llenos(self):
    	# Agregar Cita
        medico = Medico.objects.get(cedula=202020)
        user = User.objects.get(username=medico.usuario.user)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = '28-03-2017'
        hora = '7AM'
        es_referido = False

        value = agregar_citas(user_pk=user.pk,paciente=paciente.cedula,institucion=institucion.pk,
                            descripcion=descripcion,especialidad = especialidad.nombre_especialidad,
                            fecha= fecha,hora = hora, es_referido = es_referido)

        # Comenzar Revisión
        cita = Medico_Citas.objects.get(descripcion = "Nueva Cita")
        motivos = 'Dolor de Cabeza'
        sintomas = 'Vomito'
        presion_sanguinea_diastolica = 60
        presion_sanguinea_sistolica = 49
        temperatura = 32
        frec_respiratoria = 15
        frec_cardiaca = 20
        otros = 'Sintomas'

        value = comenzar_revision(cita_id = cita.id, motivos = motivos, sintomas = sintomas,
                                presion_sanguinea_diastolica = presion_sanguinea_diastolica,
                                presion_sanguinea_sistolica = presion_sanguinea_sistolica,
                                temperatura = temperatura, frec_respiratoria = frec_respiratoria,
                                frec_cardiaca = frec_cardiaca, otros = otros)

    	# Informe Médico
    	revision = Medico_Revision.objects.get(motivos = 'Dolor de Cabeza')
    	prediagnostico = 'Necesita Operacion'
        recipe_medico = 'Tomar Pildoras de Tranquilidad'

        value = informe_medico(revision_id = revision.pk, prediagnostico = prediagnostico,
                                recipe = recipe_medico)

    	self.assertIs(value, True)