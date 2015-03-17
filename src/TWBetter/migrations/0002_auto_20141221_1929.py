# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='type',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
