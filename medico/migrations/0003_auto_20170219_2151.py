# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_auto_20170218_0440'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='medico_citas',
            unique_together=set([]),
        ),
    ]
