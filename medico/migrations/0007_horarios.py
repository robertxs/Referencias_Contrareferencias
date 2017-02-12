# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0006_revisionmedico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_cita', models.DateTimeField()),
                ('disponible', models.CharField(max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')])),
                ('cedula_medico_tratante', models.ForeignKey(to='medico.Medico')),
                ('rif', models.ForeignKey(to='medico.Institucion')),
            ],
        ),
    ]
