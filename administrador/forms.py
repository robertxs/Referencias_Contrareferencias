#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from administrador.models import *


class UsuarioForm(forms.ModelForm):

    ci = forms.CharField(label="Cédula de Identidad", required=True)
    username = forms.CharField(label="Nombre de usuario", required=True)
    passw = forms.CharField(label="Contraseña", required=True,
                            widget=forms.PasswordInput())
    name = forms.CharField(label="Nombre", required=True)
    last_name = forms.CharField(label="Apellido", required=True)
    email = forms.CharField(label="Correo electrónico", required=True)

    class Meta:
        model = Usuario
        exclude = ('user',)
