# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_medico_revision'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico_revision',
            old_name='cita_id',
            new_name='cita',
        ),
    ]
