# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_auto_20170330_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fotosubida',
            field=models.BooleanField(default=False),
        ),
    ]
