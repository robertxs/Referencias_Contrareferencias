from django.shortcuts import render
from django.views.generic import *
from administrador.forms import *
from administrador.models import *


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(
            Index, self).get_context_data(**kwargs)
        return context


class Register(CreateView):
    template_name = 'register.html'
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(
            Register, self).get_context_data(**kwargs)
        return context
