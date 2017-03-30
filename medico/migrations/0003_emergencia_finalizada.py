# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_auto_20170326_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencia',
            name='finalizada',
            field=models.BooleanField(default=False),
        ),
    ]
