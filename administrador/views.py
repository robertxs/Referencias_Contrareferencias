#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import *
from administrador.forms import *
from administrador.models import *
from administrador.controllers import *


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

class Register(CreateView):
    template_name = 'register.html'
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(
            Register, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = UsuarioForm(request.POST)

        if form.is_valid():
            # Registramos al usuario
            register_user(form)
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return render_to_response('register.html',
                                      {'form': form},
                                      context_instance=RequestContext(
                                          request))


def authenticate_user(username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            if user is not None:
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                if user is not None:
                    return user
            except User.DoesNotExist:
                return None


def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(
            reverse_lazy('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_auth = authenticate_user(username, password)
            if user_auth is not None:
                if user_auth.is_active:
                    user = authenticate(username=user_auth.username,
                                        password=password)
                    if user:
                        login(request, user)
                        return HttpResponseRedirect(
                            reverse_lazy('home'))
                    else:
                        form.add_error(
                            None, "Tu correo o contraseña no son correctos")
                else:
                    form.add_error(None, "Aún no has confirmado tu correo.")
                    user = None
            else:
                form.add_error(
                    None, "Tu correo o contraseña no son correctos")
        else:
            context = {'form': form}
            return render_to_response('index.html', context,
                                      context_instance=RequestContext(request))

    else:
        form = LoginForm()
    context = {'form': form, 'host': request.get_host()}
    return render_to_response('index.html', context,
                              context_instance=RequestContext(request))


class Success(TemplateView):
    template_name = 'success.html'


class Home(TemplateView):
    template_name = 'home.html'


class Inbox(TemplateView):
    template_name = 'administrador/inbox.html'
