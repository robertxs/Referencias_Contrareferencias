# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0008_auto_20170228_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_revision',
            name='cita',
            field=models.ForeignKey(to='medico.Medico_Citas', unique=True),
        ),
    ]
