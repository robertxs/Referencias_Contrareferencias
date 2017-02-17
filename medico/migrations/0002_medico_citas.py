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
            name='Medico_Citas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
    ]
