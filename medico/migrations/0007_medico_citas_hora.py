# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0006_auto_20170304_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico_citas',
            name='hora',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
