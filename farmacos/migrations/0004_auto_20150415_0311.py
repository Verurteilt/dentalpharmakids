# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacos', '0003_farmacoicono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmacoicono',
            name='farmaco',
        ),
        migrations.DeleteModel(
            name='FarmacoIcono',
        ),
        migrations.AddField(
            model_name='farmaco',
            name='clave',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulasubfarmaco',
            name='formulario_html',
            field=models.TextField(default='hola'),
            preserve_default=False,
        ),
    ]
