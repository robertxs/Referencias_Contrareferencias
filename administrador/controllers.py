from administrador.models import *
from paciente.models import *
from medico.models import *
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


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
        'ver_usuarios'))


def agregar_rol(name):
    try:
        group = Group(name=name)
        group.save()
        return True
    except:
        return False


def eliminar_rol(request,pk):
    rol = Group.objects.get(pk=pk)
    if (rol.name == 'admin') or (rol.name == 'medico') or (rol.name == 'paciente'):
        messages.error(request,"No se puede eliminar este rol.")
    else :
        rol.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_roles'))


def agregar_institucion(rif, nombre, direccion,tipo):
    try:
        institucion = Institucion(rif=rif,
                            name = nombre,
                            address =direccion,
                            tipo = tipo)
        institucion.save()
        return True
    except:
        return False


def modificar_institucion(inst_id, direccion, tipo):
    try:
        institucion = Institucion.objects.get(pk=inst_id)
        institucion.address = direccion
        institucion.tipo = tipo
        institucion.save()
        return True
    except:
        return False


def eliminar_institucion(request, pk):
    institucion = Institucion.objects.get(pk=pk)
    institucion.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_instituciones'))

def agregar_laboratorio(rif, nombre, direccion, regente, institucion):
    try:
        laboratorio = Laboratorio(rif=rif,
                            name = nombre,
                            address = direccion,
                            regent = regente,
                            institucion = institucion
                            )
        laboratorio.save()
        return True
    except:
        return False


def modificar_laboratorio(lab_id, rif, nombre, direccion, regente):
    try:
        laboratorio = Laboratorio.objects.get(pk=lab_id)
        #laboratorio.institucion = institucion
        laboratorio.rif = rif
        laboratorio.name = nombre
        laboratorio.address = direccion
        laboratorio.regent = regente
        laboratorio.save()
        return True
    except:
        return False


def eliminar_laboratorio(request, pk):
    laboratorio = Laboratorio.objects.get(pk=pk)
    laboratorio.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_laboratorios'))

def agregar_especialidad(nombre):
    try:
        especialidad = Especialidad(nombre_especialidad = nombre)
        especialidad.save()
        return True
    except:
        return False


def modificar_especialidad(anterior, nombre):
    try:
        especialidad = Especialidad.objects.get(nombre_especialidad=anterior)
        especialidad.delete()
        especialidad = Especialidad(nombre_especialidad = nombre)
        especialidad.save()
        return True
    except:
        return False

def eliminar_especialidad(request, pk):
    especialidad = Especialidad.objects.get(pk=pk)
    especialidad.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_especialidades'))
    
def agregar_tipodeexamen(nombre):
    try:
        tipoexamen = Tipoexamen(nombretipo = nombre)
        tipoexamen.save()
        return True
    except:
        return False


def modificar_tipodeexamen(anterior, nombre):
    try:
        tipoexamen = Tipoexamen.objects.get(nombretipo=anterior)
        tipoexamen.delete()
        tipoexamen = Tipoexamen(nombretipo = nombre)
        tipoexamen.save()
        return True
    except:
        return False

def eliminar_tipodeexamen(request, pk):
    tipoexamen = Tipoexamen.objects.get(pk=pk)
    tipoexamen.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_tiposdeexamen'))
    
def eliminar_medicion(request, pk):
    medicion = Medicion.objects.get(pk=pk)
    tipoexamen = Tipoexamen.objects.filter(nombretipo=medicion.tipoexamen)
    medicion.delete()
    return HttpResponseRedirect(reverse_lazy(
        'ver_mediciones'))

def agregar_medicion(medicion,unidad,rangoesperado,posicion, tipoexamen):
    try:
        medicion = Medicion(nombremedicion=medicion,
                            tipoexamen=tipoexamen,
                            unidad=unidad,
                            rangoesperado=rangoesperado,
                            posicion=posicion
                            )
        medicion.save()
        return True
    except:
        return False
    
def modificar_medicion(medicion, nombremedicion, unidad, rangoesperado, posicion ):
    try:
        medicion = Medicion.objects.get(pk=medicion)
        tipoexamen = medicion.tipoexamen
        medicion.delete()
        medicion = Medicion(nombremedicion=nombremedicion,
                            tipoexamen=tipoexamen,
                            unidad=unidad,
                            rangoesperado=rangoesperado,
                            posicion=posicion
                            )
        medicion.save()
        return True
    except:
        return False
    




'''
def ordenar_mediciones(request):
    pks = request.POST.getlist('id')
    for pk in pks:
        posicion = request.POST['posicion_' + id]
        medicion = Medicion.objects.get(id=id)
        medicion.posicion = posicion
        medicion.save()
    tipoexamen = Tipoexamen.objects.get(pk=medicion.tipoexamen.pk)
    return HttpResponseRedirect(reverse_lazy(
'ver_mediciones', kwargs={'pk': tipoexamen.pk}))
'''

