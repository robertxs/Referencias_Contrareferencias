# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0007_medico_citas_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico_citas',
            name='especialidad',
            field=models.ForeignKey(default='', to='medico.Especialidad'),
            preserve_default=False,
        ),
    ]
