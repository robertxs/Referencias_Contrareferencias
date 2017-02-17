# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0006_auto_20170217_1906'),
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
                ('institucion', models.ForeignKey(to='medico.Institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conclusiones', models.TextField()),
                ('recipe_medico', models.TextField()),
                ('cita', models.ForeignKey(to='medico.Medico_Citas')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especialidad', models.ForeignKey(to='medico.Especialidad')),
                ('institucion', models.ForeignKey(to='medico.Institucion')),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_referencia', models.DateField()),
                ('hora_referencia', models.DateTimeField()),
                ('informe', models.ForeignKey(to='medico.Medico_Informe')),
                ('medico_referido', models.ForeignKey(to='medico.Medico')),
            ],
        ),
    ]
