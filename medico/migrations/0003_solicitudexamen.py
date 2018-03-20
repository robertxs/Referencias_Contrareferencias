# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '__first__'),
        ('medico', '0002_auto_20180320_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('laboratorio', models.ForeignKey(to='medico.Laboratorio')),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
                ('tipoexamen', models.ForeignKey(to='paciente.Tipoexamen')),
            ],
        ),
    ]
