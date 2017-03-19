# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_auto_20170317_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencia',
            name='archivo',
            field=models.FileField(upload_to=b'', verbose_name=b'informes/'),
        ),
    ]
