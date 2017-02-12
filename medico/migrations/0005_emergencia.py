# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0004_diagnostico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_entrada', models.DateField()),
                ('hora_entrada', models.DateTimeField()),
                ('cedula_medico', models.ForeignKey(to='medico.Medico')),
                ('cedula_paciente', models.ForeignKey(to='paciente.Paciente')),
                ('rif_centro_emerg', models.ForeignKey(to='medico.Institucion')),
            ],
        ),
    ]
