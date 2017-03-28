from django.test import TestCase
from medico.models import *
from medico.controllers import *
from administrador.models import *
from django.contrib.auth.models import User

class MedicoTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="usuario1",password="g4g4")
        usuario1=User.objects.get(username="usuario1")
        Usuario.objects.create(user=usuario1, ci="1111")
        usuariouno=Usuario.objects.get(ci="1111")
        Medico.objects.create(cedula=202020,first_name="roberto",last_name="rinaldi",
            fecha_nacimiento="2015-02-15",sexo="m",estado_civil="s",telefono="02125555",
            direccion="dir", usuario=usuariouno)



    def test_editar_medico_first_name(self):
        med = Medico.objects.get(cedula=202020)
        editar_medico(user=med, nombre=140, apellido="r", fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.first_name,140)

        editar_medico(user=med, nombre="ttttttttttttttttttttttttttttttttttt", apellido="r",
                      fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.first_name,"ttttttttttttttttttttttttttttttttttt")

    def test_editar_medico_last_name(self):
        med = Medico.objects.get(cedula=202020)
        editar_medico(user=med, nombre="r", apellido=33, fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.last_name,33)

        editar_medico(user=med, nombre="r", apellido="ttttttttttttttttttttttttttttttttttt",
                      fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="021255550", direccion="dir")
        self.assertNotEqual(med.last_name,"ttttttttttttttttttttttttttttttttttt")

    def test_editar_medico_telefono(self):
        med = Medico.objects.get(cedula=202020)
        editar_medico(user=med, nombre="r", apellido="r", fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="s",telefono="02125555000000000000", direccion="dir")
        self.assertNotEqual(med.telefono,"02125555000000000000")


    def test_editar_medico_estado_civil(self):
        med = Medico.objects.get(cedula=202020)
        editar_medico(user=med, nombre="r", apellido="r", fecha="2015-02-15", email="d@g.com", sexo="m",
                      estado_civil="c",telefono="02125555000", direccion="dir")
        self.assertEqual(med.estado_civil,"s")
