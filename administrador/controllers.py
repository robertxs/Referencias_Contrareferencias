from administrador.models import *
from administrador.forms import *
from django.contrib.auth.models import User, Group


def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    print("USUARIOOOO", save_user)
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    print(user)
    role = form.cleaned_data['rol']
    x, boole = Group.objects.get_or_create(name = role)
    print(x)
    group = Group.objects.get(name=x)
    user.groups.add(group)
    return user
