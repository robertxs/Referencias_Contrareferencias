from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User)
    ci = models.CharField(max_length=100, blank=False, default='')
    foto = models.ImageField(upload_to='images/', blank=True)
    fotosubida = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username


class Inbox(models.Model):
    usuario = models.ForeignKey(Usuario,
                                on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100, blank=False)
    enviado_por = models.CharField(max_length=100, blank=False)
