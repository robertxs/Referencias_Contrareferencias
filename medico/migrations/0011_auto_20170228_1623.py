# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0010_auto_20170228_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico_revision',
            name='id',
        ),
        migrations.AlterField(
            model_name='medico_revision',
            name='cita',
            field=models.OneToOneField(primary_key=True, serialize=False, to='medico.Medico_Citas'),
        ),
    ]
