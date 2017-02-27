# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0005_auto_20170227_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_revision',
            name='otros',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
