# -*- coding: utf-8 -*-
from django.test import TestCase
from datetime import datetime
from  medico.forms import*
from  medico.controllers import *
from  medico.models import *
from  paciente.models import *

##############################################
#                 Medico_Citas
##############################################

class AgregarCitasTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="usuario1",password="g4g4")
        usuario1=User.objects.get(username="usuario1")
        Usuario.objects.create(user=usuario1, ci="1111")
        usuariouno=Usuario.objects.get(ci="1111")
        Medico.objects.create(cedula=202020,first_name="roberto",last_name="rinaldi",
            fecha_nacimiento="2015-02-15",sexo="m",estado_civil="s",telefono="02125555",
            direccion="dir", usuario=usuariouno)

        medico=Medico.objects.get(cedula=202020)

        User.objects.create(username="paciente",password="123")
        paciente=User.objects.get(username="paciente")
        Usuario.objects.create(user=paciente, ci="12345678")
        paciente1=Usuario.objects.get(ci="12345678")
        Paciente.objects.create(cedula = 12345678, first_name = "Cinthya", last_name = "Ramos",
                                usuario = paciente1)
        Institucion.objects.create(rif=666555446, name = "Centro Medico La Trinidad",
                                    address = "La Trinidad")

        institucion= Institucion.objects.get(rif=666555446)

        Especialidad.objects.create(nombre_especialidad='Cardiologia')

        especialidad= Especialidad.objects.get(nombre_especialidad='Cardiologia')

        Medico_Especialidad.objects.create(especialidad=especialidad, medico=medico, institucion=institucion,
                             horario=['Lunes8AM','Martes7AM'])

# Caso Malicia
    def test_campos_vacios(self):
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

# Casos Bordes
    def test_un_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = ''
        institucion = ''
        descripcion = ''
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_dos_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = ''
        descripcion = ''
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_tres_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = ''
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_cuatro_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = ''
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_cinco_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = ''
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_seis_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = 23-04-2017
        hora = ''
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    def test_siete_campos_lleno(self):

        medico = Medico.objects.get(cedula=202020)
        paciente = Paciente.objects.get(cedula = 12345678)
        institucion = Institucion.objects.get(rif = 666555446)
        descripcion = 'Nueva Cita'
        especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
        fecha = 23-04-2017
        hora = '7 AM'
        es_referido = ''

        value = agregar_citas(user_pk=medico,paciente=paciente,institucion=institucion,
                              descripcion=descripcion,especialidad = especialidad,
                             fecha= fecha,hora = hora, es_referido = es_referido)
        self.assertIs(value, False)

    # def test_todos_campos_lleno(self):
    #
    #     medico = User.objects.get(username="usuario1")
    #     print(medico.pk)
    #     paciente = Paciente.objects.get(cedula = 12345678)
    #     institucion = Institucion.objects.get(rif = 666555446)
    #     descripcion = 'Nueva Cita'
    #     especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
    #     fecha = datetime.strptime(('2017-04-17'),"%Y-%m-%d")
    #     hora = '8AM'
    #     es_referido = False
    #
    #     value = agregar_citas(user_pk=medico.pk,paciente=paciente.cedula,institucion=institucion.rif,
    #                           descripcion=descripcion,especialidad = especialidad,
    #                          fecha= fecha,hora = hora, es_referido = es_referido)
    #     self.assertIs(value, True)

# Caso Borde, el medico no atiende en esa fecha

    # def test_fecha_invalida(self):
    #
    #     medico = User.objects.get(username="usuario1")
    #     paciente = Paciente.objects.get(cedula = 12345678)
    #     institucion = Institucion.objects.get(rif = 666555446)
    #     descripcion = 'Nueva Cita'
    #     especialidad = Especialidad.objects.get(nombre_especialidad='Cardiologia')
    #     fecha = datetime.strptime(('2017-04-07'),"%Y-%m-%d")
    #     hora = '11AM'
    #     es_referido = False
    #
    #     value = agregar_citas(user_pk=medico.pk,paciente=paciente.cedula,institucion=institucion.rif,
    #                           descripcion=descripcion,especialidad = especialidad,
    #                          fecha= fecha,hora = hora, es_referido = es_referido)
    #     print(value)
    #     self.assertIs(value, False)
