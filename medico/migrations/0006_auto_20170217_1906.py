# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0005_medico_informe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico_informe',
            old_name='sintomas_signos',
            new_name='medico_Revision',
        ),
    ]
