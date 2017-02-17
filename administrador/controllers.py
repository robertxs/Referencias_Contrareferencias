from administrador.models import *
from paciente.models import *
from medico.models import *
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


def register_user(form):
    # Almacenamos el usuario
    save_user = form.save()
    # Agregamos al usuario al grupo de acuerdo al rol
    user = User.objects.get(username=save_user.username)
    usuario = Usuario(user=user, ci=form.cleaned_data['ci'])
    usuario.save()
    group = Group.objects.get(name=form.cleaned_data['rol'])
    user.groups.add(group)
    if form.cleaned_data['rol'] == 'paciente':
        paciente = Paciente(cedula=usuario.ci, usuario=usuario,
                            first_name=user.first_name,
                            last_name=user.last_name)
        paciente.save()
    elif form.cleaned_data['rol'] == 'medico':
        medico = Medico(cedula=usuario.ci, usuario=usuario,
                        first_name=user.first_name,
                        last_name=user.last_name)
        medico.save()
    return user


def modificar_usuario(usuario_id, username, first_name,
                      last_name, email, rol):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        user = User.objects.get(pk=usuario.user.pk)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        group = Group.objects.get(name=rol)
        user.groups.remove(usuario.user.groups.all()[0])
        user.groups.add(group)
        usuario.save()
        user.save()
        return True
    except:
        return False


def eliminar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    user = User.objects.get(pk=usuario.user.pk)
    usuario.delete()
    user.delete()
    return HttpResponseRedirect(reverse_lazy(
        'historias_clinicas'))


def agregar_rol(request, name):
    group = Group(name=name)
    group.save()
    data = {'role': name}
    return HttpResponse(json.dumps(data), status=200,
                        content_type='application/json')
