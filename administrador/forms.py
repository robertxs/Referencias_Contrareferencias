#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from administrador.models import *


class UsuarioForm(forms.ModelForm):

    rol = forms.ChoiceField(
        required=True,
        choices=[
            ('admin', 'Administrador'),
            ('medico', 'Medico'),
            ('paciente', 'Paciente'),
        ]
    )

    ci = forms.CharField(required=True, label="Cédula de identidad")
    username = forms.CharField(required=True, label="Nombre de usuario")
    passw = forms.CharField(label="Contraseña", required=True,
                            widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

        error_messages = {
            'first_name': {
                'required': "Este campo es requerido"
            },
            'last_name': {
                'required': "Este campo es requerido"
            },
            'ci': {
                'required': "Este campo es requerido"
            }
        }

        widgets = {
            'email': forms.TextInput(attrs={'required': 'true'}),
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'})
        }

        labels = {
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count() != 0:
            raise forms.ValidationError(u'Este nombre de usuario ya está siendo utilizado.')
        return username

    # def clean(self):
    #     data = self.cleaned_data
    #     print("aquiiiii!")
    #     print(data)
    #     print(self)
    #     username = self.cleaned_data.get('username')
    #     # institucion = self.cleaned_data.get('institucion')
    #     # user = User.objects.get(pk=self.medico)
    #     # usuario = Usuario.objects.get(user=user)
    #     # med = Medico.objects.get(usuario=usuario)
    #     # medico = med.cedula
    #     # inst = Institucion.objects.get(name=institucion)
    #     # institucion = inst.rif
    #     # num_horarios = Medico_Especialidad.objects.filter(medico=medico,
    #     #     institucion=institucion, especialidad=especialidad).count()
    #     # print(num_horarios)

    #     # if num_horarios == 1:
    #     #     msj="Ya tiene horarios para esta especialidad en esta institución, seleccione otros por favor."
    #     #     self.add_error('especialidad',msj)

    #     if User.objects.filter(username=username).count() != 0:
    #         msj="Este nombre de usuario ya está siendo utilizado."
    #         self.add_error('username',msj)

    #     return data


    def save(self, commit=True):
        print("ENTROOO EN SAVE DE ADMIN!")
        user = super(UsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = 1
        password = self.cleaned_data['passw']
        user.set_password(password)
        user.save()
        return user


class ModificarUsuarioForm(forms.ModelForm):

    rol = forms.ChoiceField(
        required=True,
        choices=[
            ('admin', 'Administrador'),
            ('medico', 'Medico'),
            ('paciente', 'Paciente'),
        ]
    )

    ci = forms.CharField(required=True, label="Cédula de identidad")
    username = forms.CharField(required=True, label="Nombre de usuario")
    passw = forms.CharField(label="Contraseña", required=True,
                            widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

        error_messages = {
            'first_name': {
                'required': "Este campo es requerido"
            },
            'last_name': {
                'required': "Este campo es requerido"
            },
            'ci': {
                'required': "Este campo es requerido"
            }
        }

        widgets = {
            'email': forms.TextInput(attrs={'required': 'true'}),
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'})
        }

        labels = {
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }


    def save(self, commit=True):
        print("ENTROOO EN SAVE DE ADMIN DE MODIFICAR!")
        user = super(UsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = 1
        password = self.cleaned_data['passw']
        user.set_password(password)
        user.save()
        return user


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=60, required=True,
        label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Clave'}), required=True, label='')
