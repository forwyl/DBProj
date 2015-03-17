# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0008_auto_20141225_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='user',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_background',
        ),
        migrations.AddField(
            model_name='comment',
            name='ranking',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
