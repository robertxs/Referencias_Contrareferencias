# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudexamen',
            name='laboratorio',
        ),
        migrations.RemoveField(
            model_name='solicitudexamen',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='solicitudexamen',
            name='tipoexamen',
        ),
        migrations.DeleteModel(
            name='SolicitudExamen',
        ),
    ]
