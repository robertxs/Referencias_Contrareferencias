# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0003_auto_20170308_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_entrada', models.DateField()),
                ('hora_entrada', models.DateTimeField()),
                ('institucion', models.ForeignKey(to='medico.Institucion')),
                ('medico', models.ForeignKey(to='medico.Medico')),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conclusiones', models.TextField()),
                ('recipe_medico', models.TextField()),
                ('cita', models.ForeignKey(to='medico.Medico_Citas')),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_referencia', models.DateField()),
                ('hora_referencia', models.DateTimeField()),
                ('informe', models.ForeignKey(to='medico.Medico_Informe')),
                ('medico_referido', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='emergencia',
            unique_together=set([('paciente', 'medico', 'institucion')]),
        ),
    ]
