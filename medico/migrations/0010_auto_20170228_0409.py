# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0009_auto_20170228_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_informe',
            name='desc_prediagnostico',
            field=models.TextField(max_length=100),
        ),
    ]
