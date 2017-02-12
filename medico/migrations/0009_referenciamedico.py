# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0008_referencialaboratorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenciaMedico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_referencia', models.DateField()),
                ('hora_referencia', models.DateTimeField()),
                ('cedula_medico_referido', models.ForeignKey(to='medico.Medico')),
                ('cita_id', models.ForeignKey(to='medico.Cita')),
            ],
        ),
    ]
