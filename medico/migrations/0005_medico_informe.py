# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0004_auto_20170217_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico_Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc_prediagnostico', models.TextField()),
                ('cita', models.ForeignKey(to='medico.Medico_Citas')),
                ('sintomas_signos', models.ForeignKey(to='medico.Medico_Revision')),
            ],
        ),
    ]
