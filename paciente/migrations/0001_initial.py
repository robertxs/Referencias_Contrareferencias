# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Historiadetriaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medico_triaje', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edad', models.IntegerField()),
                ('tipo_sanguineo', models.CharField(max_length=20)),
                ('alergias', models.CharField(max_length=100)),
                ('adicciones', models.CharField(max_length=100)),
                ('antecedentes_familiares', models.TextField()),
                ('cedula', models.ForeignKey(to='administrador.Usuario')),
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
