# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_informemedico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conclusiones', models.TextField()),
                ('recipe_medico', models.TextField()),
                ('cita_id', models.ForeignKey(to='medico.Cita')),
            ],
        ),
    ]
