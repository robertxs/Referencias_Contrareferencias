#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from medico.models import *
from django.contrib.auth.models import User, Group
from administrador.models import Usuario
from medico.models import Medico
from paciente.models import Historiadetriaje, Paciente
import datetime

class Paciente_CitasForm(forms.ModelForm):

    class Meta:
        model = Medico_Citas
        exclude = ("paciente",)
        fields = ['medico','institucion', 'fecha','descripcion']


    def clean_fecha(self):
        fecha_cita = self.cleaned_data.get('fecha')

        #Obtenemos la fecha actual
        fecha_actual = datetime.datetime.now().date()
        if fecha_cita < fecha_actual :
            raise forms.ValidationError('La fecha de la cita no puede ser menor a la de hoy')

        return fecha_cita
