#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from medico.models import *
from django.contrib.auth.models import User, Group
from administrador.models import Usuario
from medico.models import Medico
from paciente.models import Historiadetriaje, Paciente
import datetime


class Medico_EstudiosForm(forms.ModelForm):

    class Meta:
        model = Medico_Estudios
        exclude = ("medico",)


class Medico_LogrosForm(forms.ModelForm):

    class Meta:
        model = Medico_Logros
        exclude = ("medico",)


class Medico_PublicacionesForm(forms.ModelForm):

    class Meta:
        model = Medico_Publicaciones
        exclude = ("medico",)


class Medico_ExperienciasForm(forms.ModelForm):

    class Meta:
        model = Medico_Experiencias
        exclude = ("medico",)


class Medico_HabilidadesForm(forms.ModelForm):

    class Meta:
        model = Medico_Habilidades
        exclude = ("medico",)


class Medico_EventosForm(forms.ModelForm):

    class Meta:
        model = Medico_Eventos
        exclude = ("medico",)


class Medico_CitasForm(forms.ModelForm):

    class Meta:
        model = Medico_Citas
    #    exclude = ("medico",)
        fields = ['paciente','institucion', 'fecha','descripcion']
        # '__all__'

    def clean_fecha(self):
        fecha_cita = self.cleaned_data.get('fecha')
        num_pacientes= Medico_Citas.objects.filter(fecha=fecha_cita).count()
        print(num_pacientes)
        print(fecha_cita)
        #Obtenemos la fecha actual
        fecha_actual = datetime.datetime.now().date()
        if fecha_cita < fecha_actual :
            raise forms.ValidationError('La fecha de la cita no puede ser menor a la de hoy')

        if num_pacientes > 10:
            raise forms.ValidationError('La fecha solicitada no se encuentra disponible')
        return fecha_cita



class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = Historiadetriaje
        fields = ["paciente", "medico_triaje", "antecedentes_personales", "antecedentes_familiares", "motivo_consulta",
                "enfermedad_actual", "peso", "talla", "signos_vitales", "piel", "ojos",
                "fosas_nasales", "conductos_auditivos", "cavidad_oral", "cuello",
                "columna", "torax", "abdomen", "extremidades", "genitales"]

        # widgets = {
        #     'antecedentes_personales': forms.Textarea(),
        #     'antecedentes_familiares': forms.Textarea()
        # }

    def __init__(self, *args, **kwargs):
        super(HistoriaClinicaForm, self).__init__(*args, **kwargs)
        self.fields['paciente'].queryset = Paciente.objects.all()
        # self.fields['medico'].queryset = Paciente.objects.all()


class Medico_ConsultasForm(forms.ModelForm):

    class Meta:
        model = Medico_Citas
        fields = ("paciente", "institucion", "fecha")

        labels = {
            'paciente' : 'Paciente',
            'institucion' : 'Institución',
            'fecha' : 'Fecha',
        }
