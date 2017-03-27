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
                ('hora', models.CharField(max_length=5, choices=[(b'6Am', b'6Am'), (b'7Am', b'7Am'), (b'8Am', b'8Am'), (b'9Am', b'9Am'), (b'10Am', b'10Am'), (b'11Am', b'11Am'), (b'12Pm', b'12Pm'), (b'1Pm', b'1Pm'), (b'2Pm', b'2Pm'), (b'3Pm', b'3Pm'), (b'4Pm', b'4Pm'), (b'5Pm', b'5Pm')])),
                ('revision', models.BooleanField(default=False)),
                ('informe', models.BooleanField(default=False)),
                ('es_referido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Diagnostico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conclusiones', models.TextField()),
                ('recipe_medico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc_prediagnostico', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('hora', models.CharField(max_length=5, choices=[(b'6Am', b'6Am'), (b'7Am', b'7Am'), (b'8Am', b'8Am'), (b'9Am', b'9Am'), (b'10Am', b'10Am'), (b'11Am', b'11Am'), (b'12Pm', b'12Pm'), (b'1Pm', b'1Pm'), (b'2Pm', b'2Pm'), (b'3Pm', b'3Pm'), (b'4Pm', b'4Pm'), (b'5Pm', b'5Pm')])),
                ('archivo', models.FileField(upload_to=b'informes/')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Revision',
            fields=[
                ('cita', models.OneToOneField(primary_key=True, serialize=False, to='medico.Medico_Citas')),
                ('motivos', models.CharField(max_length=500)),
                ('sintomas', models.CharField(max_length=500)),
                ('presion_sanguinea', models.CharField(max_length=30)),
                ('temperatura', models.CharField(max_length=500)),
                ('frec_respiratoria', models.CharField(max_length=500)),
                ('frec_cardiaca', models.CharField(max_length=50)),
                ('otros', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='referencia',
            name='cita',
            field=models.ForeignKey(to='medico.Medico_Citas'),
        ),
        migrations.AddField(
            model_name='referencia',
            name='especialidad',
            field=models.ForeignKey(to='medico.Especialidad'),
        ),
        migrations.AddField(
            model_name='referencia',
            name='institucion',
            field=models.ForeignKey(to='medico.Institucion'),
        ),
        migrations.AddField(
            model_name='referencia',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='referencia',
            name='paciente',
            field=models.ForeignKey(to='paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='medico_diagnostico',
            name='cita',
            field=models.ForeignKey(to='medico.Medico_Citas'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='especialidad',
            field=models.ForeignKey(to='medico.Especialidad'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='institucion',
            field=models.ForeignKey(to='medico.Institucion'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='medico',
            field=models.ForeignKey(to='medico.Medico'),
        ),
        migrations.AddField(
            model_name='medico_citas',
            name='paciente',
            field=models.ForeignKey(to='paciente.Paciente'),
        ),
        migrations.AddField(
            model_name='medico_informe',
            name='medico_Revision',
            field=models.ForeignKey(to='medico.Medico_Revision'),
        ),
        migrations.AlterUniqueTogether(
            name='medico_citas',
            unique_together=set([('paciente', 'medico', 'institucion', 'fecha')]),
        ),
        migrations.AlterUniqueTogether(
            name='emergencia',
            unique_together=set([('paciente', 'medico', 'institucion')]),
        ),
    ]
