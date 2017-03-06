# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0008_medico_citas_especialidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_citas',
            name='hora',
            field=models.CharField(max_length=5, choices=[(b'6Am', b'6Am'), (b'7Am', b'7Am'), (b'8Am', b'8Am'), (b'9Am', b'9Am'), (b'10Am', b'10Am'), (b'11Am', b'11Am'), (b'12pm', b'12pm'), (b'1pm', b'1pm'), (b'2pm', b'2pm'), (b'3pm', b'3pm'), (b'4pm', b'4pm'), (b'5pm', b'5pm')]),
        ),
    ]
