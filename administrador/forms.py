#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
#from django.core.validators import validate_email
from administrador.models import *
from django.contrib.auth.models import User, Group
from medico.models import *


class UsuarioForm(forms.ModelForm):

    name_validator = RegexValidator(
    regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\- ]+$',
    message = 'La entrada debe ser un nombre en Español sin símbolos especiales.')

    email_validator = RegexValidator(
        regex   = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
        message = 'La dirección de correo electrónico debe ser de la forma: correo@xxx.com.')

    ci_validator = RegexValidator(
        regex   = '^[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma')

    first_name = forms.CharField(
            required   = True,
            label      = "Nombre",
            validators = [name_validator],
            widget     = forms.TextInput(attrs =
                { 'placeholder' : 'Nombre'
                , 'required' : 'true'
                , 'pattern'     : name_validator.regex.pattern
                , 'message'     : name_validator.message

                }
            )
    )

    last_name = forms.CharField(
            required   = True,
            label      = "Apellido",
            validators = [name_validator],
            widget     = forms.TextInput(attrs =
                { 'placeholder' : 'Apellido'
                , 'required'    : 'true'
                , 'pattern'     : name_validator.regex.pattern
                , 'message'     : name_validator.message

                }
            )
    )

    rol = forms.ChoiceField(
        required=True,
        choices=[
            ('admin', 'Administrador'),
            ('medico', 'Medico'),
            ('paciente', 'Paciente'),
        ]
    )

    email = forms.CharField(
            required = True,
            label = "Correo Electrónico",
            validators = [email_validator],
            widget = forms.TextInput(attrs =
            {'placeholder' : "Correo"
             , 'required'  : 'true'
             , 'pattern'   : email_validator.regex.pattern
             , 'message'   : email_validator.message
             }
            )
    )

    ci = forms.CharField(
            required=True,
            label="Cédula de Identidad",
            validators=[ci_validator],
            widget = forms.TextInput(attrs=
            { 'placeholder': "Cédula"
              , 'required':'true'
              , 'pattern' : ci_validator.regex.pattern
              , 'message' : ci_validator.message}))

#    foto = forms.ImageField(required = False)
    username = forms.CharField(required=True, label="Nombre de usuario")
    passw = forms.CharField(label="Contraseña", required=True,
                            widget=forms.PasswordInput())

    print(username)
    #print(foto)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count() != 0:
            raise forms.ValidationError(u'Este nombre de usuario ya está siendo utilizado.')
        return username

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


class ModificarUsuarioForm(forms.ModelForm):

    print("raro raro")

    name_validator = RegexValidator(
    regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\- ]+$',
    message = 'La entrada debe ser un nombre en Español sin símbolos especiales.')

    email_validator = RegexValidator(
        regex   = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
        message = 'La dirección de correo electrónico debe ser de la forma: correo@xxx.com.')

    ci_validator = RegexValidator(
        regex   = '^[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma')

    first_name = forms.CharField(
            required   = True,
            label      = "Nombre",
            validators = [name_validator],
            widget     = forms.TextInput(attrs =
                { 'placeholder' : 'Nombre'
                , 'required' : 'true'
                , 'pattern'     : name_validator.regex.pattern
                , 'message'     : name_validator.message

                }
            )
    )

    last_name = forms.CharField(
            required   = True,
            label      = "Apellido",
            validators = [name_validator],
            widget     = forms.TextInput(attrs =
                { 'placeholder' : 'Apellido'
                , 'required'    : 'true'
                , 'pattern'     : name_validator.regex.pattern
                , 'message'     : name_validator.message

                }
            )
    )

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
    print("oooohhhhh")
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


class InstitucionFormEditar(forms.ModelForm):

    class Meta:
        model = Institucion
        exclude = ["rif","name"]


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        nombre = self.cleaned_data.get('nombre_especialidad')

        cantidad = Especialidad.objects.filter(nombre_especialidad=nombre).count()

        if cantidad == 1:
            msj="Ya existe este nombre de especialidad, verifíquelo por favor."
            self.add_error('nombre_especialidad',msj)

class RolesForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'


class PerfilForm(forms.ModelForm):

    name_validator = RegexValidator(
    regex   = '^[A-Za-záéíóúñÑÁÉÍÓÚäëïöüÄËÏÖÜ\'\- ]+$',
    message = 'La entrada debe ser un nombre en Español sin símbolos especiales.')

    email_validator = RegexValidator(
        regex   = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
        message = 'La dirección de correo electrónico debe ser de la forma: correo@xxx.com.')

    ci_validator = RegexValidator(
        regex   = '^[1-9][0-9]{4}[0-9]+$',
        message = 'Introduzca un CI con un formato válido de la forma')

    first_name = forms.CharField(
            required   = True,
            label      = "Nombre",
            validators = [name_validator],
            widget     = forms.TextInput(attrs =
                { 'placeholder' : 'Nombre'
                , 'required' : 'true'
                , 'pattern'     : name_validator.regex.pattern
                , 'message'     : name_validator.message

                }
            )
    )

    last_name = forms.CharField(
            required   = True,
            label      = "Apellido",
            validators = [name_validator],
            widget     = forms.TextInput(attrs =
                { 'placeholder' : 'Apellido'
                , 'required'    : 'true'
                , 'pattern'     : name_validator.regex.pattern
                , 'message'     : name_validator.message

                }
            )
    )

    rol = forms.ChoiceField(
        required=True,
        choices=[
            ('admin', 'Administrador'),
            ('medico', 'Medico'),
            ('paciente', 'Paciente'),
        ]
    )

    email = forms.CharField(
            required = True,
            label = "Correo Electrónico",
            validators = [email_validator],
            widget = forms.TextInput(attrs =
            {'placeholder' : "Correo"
             , 'required'  : 'true'
             , 'pattern'   : email_validator.regex.pattern
             , 'message'   : email_validator.message
             }
            )
    )

    ci = forms.CharField(
            required=True,
            label="Cédula de Identidad",
            validators=[ci_validator],
            widget = forms.TextInput(attrs=
            { 'placeholder': "Cédula"
              , 'required':'true'
              , 'pattern' : ci_validator.regex.pattern
              , 'message' : ci_validator.message}))

    foto = forms.ImageField(required = False)
    username = forms.CharField(required=True, label="Nombre de usuario")
    passw = forms.CharField(label="Contraseña", required=True,
                            widget=forms.PasswordInput())

    print(username)
    print(foto)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).count() != 0:
            raise forms.ValidationError(u'Este nombre de usuario ya está siendo utilizado.')
        return username

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
