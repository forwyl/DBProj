# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0002_auto_20141221_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='address',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='phone',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
