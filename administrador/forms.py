#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from administrador.models import *
from django.contrib.auth.models import User, Group
from medico.models import *


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


class InstitucionForm(forms.ModelForm):

    class Meta:
        model = Institucion
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        rif = self.cleaned_data.get('rif')
        nombre = self.cleaned_data.get('name')
    
        num_rif = Institucion.objects.filter(rif=rif).count()
        print(num_rif)

        num_nombre = Institucion.objects.filter(name=nombre).count()
        print(num_nombre)

        if num_rif == 1:
            msj="Ya existe este rif asociado a una institución, verifíquelo por favor."
            self.add_error('rif',msj)

        if num_nombre == 1:
            msj="Ya existe este nombre asociado a una institución, verifíquelo por favor."
            self.add_error('name',msj)

        return data


class EspecialidadForm(forms.ModelForm):

    class Meta:
        model = Especialidad
        fields = '__all__'

class RolesForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'