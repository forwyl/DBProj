# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CASFood',
            fields=[
                ('pno', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('intro', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GFood',
            fields=[
                ('key', models.AutoField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('agrospec', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('id', models.CharField(max_length=50)),
                ('image_url', models.URLField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('spc_catalogs_id', models.CharField(max_length=50)),
                ('title', models.TextField(blank=True)),
                ('unit_price', models.TextField(blank=True)),
                ('modify_date', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('key', models.AutoField(serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('manager', models.CharField(max_length=50)),
                ('address', models.CharField(unique=True, max_length=300)),
                ('phone', models.CharField(unique=True, max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('type', models.IntegerField()),
                ('website', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gfood',
            name='producer',
            field=models.ForeignKey(to='TWBetter.Producer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='casfood',
            name='producer',
            field=models.ForeignKey(to='TWBetter.Producer'),
            preserve_default=True,
        ),
    ]
