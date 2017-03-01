# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0004_auto_20170227_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_especialidad',
            name='disponibilidad',
            field=models.CharField(default=b'Si', max_length=2, choices=[(b'Si', b'Si'), (b'No', b'No')]),
        ),
    ]
