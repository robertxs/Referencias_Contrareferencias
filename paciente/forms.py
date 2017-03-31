#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from medico.models import *
from django.contrib.auth.models import User, Group
from administrador.models import Usuario
from medico.models import Medico
from paciente.models import Historiadetriaje, Paciente
import datetime

dicDias = {'Monday':'Lunes','Tuesday':'Martes','Wednesday':'Miercoles',
            'Thursday':'Jueves','Friday':'Viernes','Saturday':'Sabado',
            'Sunday':'Domingo'}


def Conocer_dia(fecha):
    # fecha = datetime.date(anio,mes,dia)
    day = dicDias[fecha.strftime('%A')]
    return day


def volverElemlista(lista,ultimo):
    x = "'"
    indice= lista.index(x)
    if ultimo :
        return lista[indice+1:len(lista)-3]
    else :
        return lista[indice+1:len(lista)-2]


class Paciente_CitasForm(forms.ModelForm):

    class Meta:
        model = Medico_Citas
        exclude = ['paciente']
        # fields = ['medico','institucion', 'fecha','descripcion','especialidad','hora','paciente']


    def __init__(self, *args, **kwargs):
        self.paciente = kwargs.pop('paciente',None)
        super(Paciente_CitasForm,self).__init__(*args,**kwargs)


    def clean(self):
        data = self.cleaned_data
        fecha = self.cleaned_data.get('fecha')
        hora = self.cleaned_data.get('hora')
        especialidad = self.cleaned_data.get('especialidad')
        inst = self.cleaned_data.get('institucion')
        institucion = Institucion.objects.get(name=inst)
        medico = self.cleaned_data.get('medico')
        user = User.objects.get(pk=self.paciente)
        usuario = Usuario.objects.get(user=user)
        pac = Paciente.objects.get(usuario=usuario)
        paciente = pac.cedula
        try:
            cita1 = Medico_Citas.objects.get(paciente=paciente,fecha=fecha,
                hora=hora,medico=medico)
            ident = cita1.id
        except Medico_Citas.DoesNotExist:
            ident = -1

        num_paciente = Medico_Citas.objects.filter(paciente=paciente,fecha=fecha,
            hora=hora).count()
        try:
            cita2 = Medico_Citas.objects.get(paciente=paciente,fecha=fecha,
            hora=hora)
            ident2 = cita2.id
        except Medico_Citas.DoesNotExist:
            ident2 = -2

        dia= Conocer_dia(fecha)
        dia_hora=dia+hora
        cantidad = Medico_Especialidad.objects.filter(medico=medico,
            institucion=institucion.id,especialidad=especialidad).count()

        if cantidad > 0 :
            disponibilidad =Medico_Especialidad.objects.get(medico=medico,
                institucion=institucion.id,especialidad=especialidad)
            horario= disponibilidad.horario
            horario2=horario.split(', ')
            i = 0
            a = ''
            for x in horario2 :
                ulti = i == (len(horario2)-1)
                elem=volverElemlista(x,ulti)
                boo = (dia_hora == elem)
                a = a + elem + ', '
                if boo :
                    break
                i = i+1
            fecha_actual = datetime.datetime.now().date()
            if fecha < fecha_actual :
                msj = "La fecha de la cita no puede ser menor a la de hoy. "
                self.add_error('fecha',msj)

            if (num_paciente == 1) and (ident != ident2):
                msj="Cambie la hora y fecha de su consulta porque ya tiene otra cita a esa hora. "
                self.add_error('hora',msj)

            if boo :
                num_citas = Medico_Citas.objects.filter(fecha=fecha, hora=hora,
                    especialidad=especialidad,medico=medico,institucion=institucion).count()
                try:
                    cita3 = Medico_Citas.objects.get(fecha=fecha, hora=hora,
                    especialidad=especialidad,medico=medico,institucion=institucion)
                    ident3 = cita3.id
                except Medico_Citas.DoesNotExist:
                    ident3 = -3

                if (num_citas == 1) and (ident != ident3) :
                    msj = "La fecha y hora solicitadas no se encuentran disponibles. Por favor elija algunas de estos horarios: "
                    msj = msj + a
                    self.add_error('hora',msj)
            else :
                msj = "El Medico no atiende ese dia a esa hora. Por favor elija algunos de estos horarios: "
                msj = msj + a
                self.add_error('hora',msj)
        else :
            cantidad = Medico_Especialidad.objects.filter(medico=medico)
            especialidad = ''
            institucion = ''
            msj = "El Medico no atiende esta especialidad en esta institucion. Las especialidades que atiende "
            msj = msj + " en la correspondiente institucion son: "
            for c in cantidad :
                msj = msj + str(c.especialidad) + ' en ' + str(c.institucion) + ', '
            self.add_error('institucion',msj)

        return data
