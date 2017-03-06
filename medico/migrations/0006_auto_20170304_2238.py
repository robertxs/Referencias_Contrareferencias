# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0005_auto_20170227_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico_especialidad',
            name='disponibilidad',
        ),
        migrations.AlterField(
            model_name='medico_especialidad',
            name='horario',
            field=models.CharField(max_length=1000),
        ),
    ]
