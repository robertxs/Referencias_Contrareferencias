# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_paciente_revision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='revision',
        ),
    ]
