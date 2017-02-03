from administrador.models import *
from administrador.forms import *
from django.contrib.auth.models import User, Group


def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    role = form.cleaned_data['rol']
    x, boole = Group.objects.get_or_create(name = role)
    group = Group.objects.get(name=x)
    user.groups.add(group)
    return user
