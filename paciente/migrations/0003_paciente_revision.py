# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_paciente_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='revision',
            field=models.BooleanField(default=False),
        ),
    ]
