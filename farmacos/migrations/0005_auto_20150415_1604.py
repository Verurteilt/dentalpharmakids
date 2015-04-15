# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmacos', '0004_auto_20150415_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacocuadro',
            name='imagen',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
