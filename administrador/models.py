from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	TIPO = (
		('Administrador', 'Administrador'),
		('Medico', 'Medico'),
		('Paciente', 'Paciente')
	)

	ESTADOS_CIVILES = (
		('Soltero', 'Soltero'),
		('Casado', 'Casado'),
		('Viudo', 'Viudo'),
		('Divorciado','Divorciado')
	)

	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=10)
	usuario = models.CharField(max_length=10, choices=TIPO)
	ci = models.CharField(max_length=100, blank=False, default='', primary_key=True)
	estado_civil = models.CharField(max_length=7, choices=ESTADOS_CIVILES)

	def __str__(self):
		return self.user.username

class Inbox(models.Model):
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100, blank=False)
    enviado_por = models.CharField(max_length=100, blank=False)

