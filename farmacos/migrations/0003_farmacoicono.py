# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacos', '0002_formulasubfarmaco_nombre_formula'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmacoIcono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icono', models.ImageField(upload_to=b'farmacos')),
                ('bloqueado', models.BooleanField(default=False)),
                ('farmaco', models.ForeignKey(to='farmacos.Farmaco')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
