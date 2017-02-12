# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0005_emergencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='RevisionMedico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivos', models.CharField(max_length=500)),
                ('sintomas', models.TextField()),
                ('presion_sanguinea', models.CharField(max_length=30)),
                ('temperatura', models.CharField(max_length=50)),
                ('frec_respiratoria', models.CharField(max_length=50)),
                ('frec_cardiaca', models.CharField(max_length=50)),
                ('otros', models.TextField()),
                ('cita_id', models.ForeignKey(to='medico.Cita')),
            ],
        ),
    ]
