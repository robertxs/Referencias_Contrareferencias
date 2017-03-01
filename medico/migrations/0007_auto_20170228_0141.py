# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0006_auto_20170227_0516'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='medico_revision',
            unique_together=set([('cita', 'id')]),
        ),
    ]
