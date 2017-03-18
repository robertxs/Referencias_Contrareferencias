# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico_Citas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('hora', models.CharField(max_length=5, choices=[(b'6Am', b'6Am'), (b'7Am', b'7Am'), (b'8Am', b'8Am'), (b'9Am', b'9Am'), (b'10Am', b'10Am'), (b'11Am', b'11Am'), (b'12Pm', b'12Pm'), (b'1Pm', b'1Pm'), (b'2Pm', b'2Pm'), (b'3Pm', b'3Pm'), (b'4Pm', b'4Pm'), (b'5Pm', b'5Pm')])),
                ('revision', models.BooleanField(default=False)),
                ('informe', models.BooleanField(default=False)),
                ('especialidad', models.ForeignKey(to='medico.Especialidad')),
                ('institucion', models.ForeignKey(to='medico.Institucion')),
                ('medico', models.ForeignKey(to='medico.Medico')),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='medico_citas',
            unique_together=set([('paciente', 'medico', 'institucion', 'fecha')]),
        ),
    ]
