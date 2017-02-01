from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User)
    #group = models.ManyToManyField(Group)
    ci = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.user.username
