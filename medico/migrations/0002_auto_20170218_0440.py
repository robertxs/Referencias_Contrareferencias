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
            name='Medico_Citas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
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
            name='Medico_Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc_prediagnostico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivos', models.CharField(max_length=500)),
                ('sintomas', models.TextField()),
                ('presion_sanguinea', models.CharField(max_length=30)),
                ('temperatura', models.CharField(max_length=50)),
                ('frec_respiratoria', models.CharField(max_length=50)),
                ('frec_cardiaca', models.CharField(max_length=50)),
                ('otros', models.TextField()),
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
        migrations.AddField(
            model_name='medico_informe',
            name='medico_Revision',
            field=models.ForeignKey(to='medico.Medico_Revision'),
        ),
        migrations.AlterUniqueTogether(
            name='medico_citas',
            unique_together=set([('paciente', 'medico', 'institucion')]),
        ),
        migrations.AlterUniqueTogether(
            name='emergencia',
            unique_together=set([('paciente', 'medico', 'institucion')]),
        ),
    ]
