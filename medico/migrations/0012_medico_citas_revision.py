# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0011_auto_20170228_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico_citas',
            name='revision',
            field=models.BooleanField(default=False),
        ),
    ]
