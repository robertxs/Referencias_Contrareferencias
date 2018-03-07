#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from paciente.models import *
from medico.models import *
import django.apps

#aux = django.apps.apps.get_models()
#print(aux)

class ExamenForm(forms.Form):
	tipo_examen = forms.ModelChoiceField(queryset=Tipoexamen.objects.all())
	paciente = forms.ModelChoiceField(queryset=Paciente.objects.all())
	laboratorio = forms.ModelChoiceField(queryset=Laboratorio.objects.all())
	
