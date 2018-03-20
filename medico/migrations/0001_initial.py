# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '__first__'),
        ('paciente', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('nombre_especialidad', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rif', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('tipo', models.CharField(default=b'', max_length=30, choices=[(b'Hospital', b'Hospital'), (b'Clinica', b'Clinica'), (b'Laboratorio', b'Laboratorio')])),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rif', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('regent', models.CharField(max_length=100)),
                ('institucion', models.ForeignKey(to='medico.Institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('cedula', models.IntegerField(serialize=False, primary_key=True, validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('first_name', models.CharField(max_length=30, null=True, blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, blank=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('sexo', models.CharField(max_length=10, null=True, blank=True)),
                ('estado_civil', models.CharField(max_length=15, null=True, blank=True)),
                ('telefono', models.CharField(max_length=15, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('usuario', models.ForeignKey(to='administrador.Usuario')),
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
            name='Medico_Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.CharField(max_length=1000)),
                ('especialidad', models.ForeignKey(to='medico.Especialidad')),
                ('institucion', models.ForeignKey(to='medico.Institucion')),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Estudios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('fecha_graduacion', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('institucion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Eventos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('institucion', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Experiencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('institucion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Habilidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc_prediagnostico', models.TextField(max_length=100)),
                ('recipe_medico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Logros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(to='medico.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Publicaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('autores', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('revista', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('volumen', models.CharField(max_length=5)),
                ('fecha', models.DateField()),
                ('medico', models.ForeignKey(to='medico.Medico')),
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
            name='SolicitudExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('laboratorio', models.ForeignKey(to='medico.Laboratorio')),
                ('paciente', models.ForeignKey(to='paciente.Paciente')),
                ('tipoexamen', models.ForeignKey(to='paciente.Tipoexamen')),
            ],
        ),
        migrations.CreateModel(
            name='Medico_Revision',
            fields=[
                ('cita', models.OneToOneField(primary_key=True, serialize=False, to='medico.Medico_Citas')),
                ('motivos', models.CharField(max_length=500)),
                ('sintomas', models.CharField(max_length=500)),
                ('presion_sanguinea_diastolica', models.IntegerField(default=0)),
                ('presion_sanguinea_sistolica', models.IntegerField(default=0)),
                ('temperatura', models.IntegerField(default=0)),
                ('frec_respiratoria', models.IntegerField(default=0)),
                ('frec_cardiaca', models.IntegerField(default=0)),
                ('otros', models.CharField(max_length=100, blank=True)),
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
    ]
