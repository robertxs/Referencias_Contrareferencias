# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_auto_20170308_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico_Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc_prediagnostico', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Revision',
            fields=[
                ('cita', models.OneToOneField(primary_key=True, serialize=False, to='medico.Medico_Citas')),
                ('motivos', models.CharField(max_length=500)),
                ('sintomas', models.CharField(max_length=500)),
                ('presion_sanguinea', models.CharField(max_length=30)),
                ('temperatura', models.CharField(max_length=500)),
                ('frec_respiratoria', models.CharField(max_length=500)),
                ('frec_cardiaca', models.CharField(max_length=50)),
                ('otros', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='medico_informe',
            name='medico_Revision',
            field=models.ForeignKey(to='medico.Medico_Revision'),
        ),
    ]
