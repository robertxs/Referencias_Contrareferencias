# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0007_horarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenciaLaboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('examenes_estudios', models.TextField()),
                ('cita_id', models.ForeignKey(to='medico.Cita')),
            ],
        ),
    ]
