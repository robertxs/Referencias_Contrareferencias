# -*- coding: utf-8 -*-
from django.test import TestCase
from datetime import datetime
from  medico.forms import Medico_CitasForm
#from medico.models import

##############################################
#                 Medico_Citas
##############################################

class AgregarCitasFormTestCase(TestCase):

    def test_campos_vacios(self):
        form_data = {}
        form = Medico_CitasForm(data = form_data)
        self.assertFalse(form.is_valid())
