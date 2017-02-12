# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asunto', models.CharField(max_length=100)),
                ('enviado_por', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=10, choices=[(b'Administrador', b'Administrador'), (b'Medico', b'Medico'), (b'Paciente', b'Paciente')])),
                ('ci', models.CharField(default=b'', max_length=100, serialize=False, primary_key=True)),
                ('estado_civil', models.CharField(max_length=7, choices=[(b'Soltero', b'Soltero'), (b'Casado', b'Casado'), (b'Viudo', b'Viudo'), (b'Divorciado', b'Divorciado')])),
            ],
        ),
        migrations.AddField(
            model_name='inbox',
            name='usuario',
            field=models.ForeignKey(to='administrador.Usuario'),
        ),
    ]
