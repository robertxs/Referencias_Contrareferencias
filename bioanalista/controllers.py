from administrador.models import Usuario
from .models import Bioanalista
from django.contrib.auth.models import User

def get_bioanalista(user_pk):
	user = User.objects.get(pk = user_pk)
	usuario = Usuario.objects.get(user = user)
	bioanalista = Bioanalista.objects.get(usuario = usuario)
	
	return bioanalista
