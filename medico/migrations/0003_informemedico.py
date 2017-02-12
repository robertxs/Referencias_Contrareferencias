# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_cita'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformeMedico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sintomas_signos', models.TextField()),
                ('desc_prediagnostico', models.TextField()),
                ('cita_id', models.ForeignKey(to='medico.Cita')),
            ],
        ),
    ]
