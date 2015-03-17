# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0005_auto_20141221_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('key', models.AutoField(serialize=False, primary_key=True)),
                ('message', models.TextField(null=True, blank=True)),
                ('gfood', models.ForeignKey(to='TWBetter.GFood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('key', models.AutoField(serialize=False, primary_key=True)),
                ('gfood', models.ForeignKey(to='TWBetter.GFood')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_account', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('user_mail', models.EmailField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('user_membership', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(to='TWBetter.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='TWBetter.User'),
            preserve_default=True,
        ),
    ]
