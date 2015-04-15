# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulasubfarmaco',
            name='nombre_formula',
            field=models.CharField(default='Paracetamol cada 6 horas', max_length=100),
            preserve_default=False,
        ),
    ]
