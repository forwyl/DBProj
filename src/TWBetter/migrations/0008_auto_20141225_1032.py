# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TWBetter', '0007_auto_20141224_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_nickname', models.CharField(default=b'\xe9\x84\x89\xe6\xb0\x91', max_length=200)),
                ('user_image', models.ImageField(default=b'pics/default.png', upload_to=b'pics/')),
                ('user_membership', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='TWBetter.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(to='TWBetter.UserProfile'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
