# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0003_auto_20141221_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gfood',
            old_name='country',
            new_name='county',
        ),
        migrations.AddField(
            model_name='gfood',
            name='catalogs_id',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
