# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '__first__'),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especialidad', models.ForeignKey(to='medico.Especialidad')),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Historiadetriaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('antecedentes_personales', models.CharField(max_length=500)),
                ('antecedentes_familiares', models.CharField(max_length=500)),
                ('motivo_consulta', models.CharField(max_length=200)),
                ('enfermedad_actual', models.CharField(max_length=200)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
                ('talla', models.DecimalField(max_digits=5, decimal_places=2)),
                ('signos_vitales', models.CharField(max_length=200)),
                ('piel', models.CharField(max_length=200)),
                ('ojos', models.CharField(max_length=200)),
                ('fosas_nasales', models.CharField(max_length=200)),
                ('conductos_auditivos', models.CharField(max_length=200)),
                ('cavidad_oral', models.CharField(max_length=200)),
                ('cuello', models.CharField(max_length=200)),
                ('columna', models.CharField(max_length=200)),
                ('torax', models.CharField(max_length=200)),
                ('abdomen', models.CharField(max_length=200)),
                ('extremidades', models.CharField(max_length=200)),
                ('genitales', models.CharField(max_length=200)),
                ('medico_triaje', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula', models.IntegerField(serialize=False, primary_key=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('lugar_nacimiento', models.CharField(max_length=70, null=True, blank=True)),
                ('sexo', models.CharField(max_length=10, null=True, blank=True)),
                ('estado_civil', models.CharField(blank=True, max_length=7, null=True, choices=[(b'Soltero', b'Soltero'), (b'Casado', b'Casado')])),
                ('ocupacion', models.CharField(max_length=30, null=True, blank=True)),
                ('direccion', models.CharField(max_length=70, null=True, blank=True)),
                ('telefono', models.CharField(max_length=13, null=True, blank=True)),
                ('usuario', models.ForeignKey(to='administrador.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='historiadetriaje',
            name='paciente',
            field=models.ForeignKey(to='paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='historia',
            name='paciente',
            field=models.ForeignKey(to='paciente.Paciente'),
        ),
    ]
