# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('cedula_medico', models.ForeignKey(to='medico.Medico')),
                ('cedula_paciente', models.ForeignKey(to='paciente.Paciente')),
                ('especialidad', models.ForeignKey(to='medico.Especialidad')),
                ('rif_centro_medico', models.ForeignKey(to='medico.Institucion')),
            ],
        ),
    ]
