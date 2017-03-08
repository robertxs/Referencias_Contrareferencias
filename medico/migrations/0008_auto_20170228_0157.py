# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0007_auto_20170228_0141'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='medico_revision',
            unique_together=set([]),
        ),
    ]
