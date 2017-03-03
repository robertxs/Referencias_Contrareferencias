# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0012_medico_citas_revision'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico_citas',
            name='informe',
            field=models.BooleanField(default=False),
        ),
    ]
