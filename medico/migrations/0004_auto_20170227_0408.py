# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_auto_20170219_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_revision',
            name='frec_respiratoria',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='medico_revision',
            name='otros',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='medico_revision',
            name='sintomas',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='medico_revision',
            name='temperatura',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterUniqueTogether(
            name='medico_citas',
            unique_together=set([('paciente', 'medico', 'institucion', 'fecha')]),
        ),
    ]
