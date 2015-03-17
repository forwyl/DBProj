# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0006_auto_20141224_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casfood',
            name='producer',
        ),
        migrations.DeleteModel(
            name='CASFood',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_membership',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
