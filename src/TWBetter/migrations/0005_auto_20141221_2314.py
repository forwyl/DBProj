# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TWBetter', '0004_auto_20141221_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casfood',
            name='intro',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casfood',
            name='name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='casfood',
            name='producer',
            field=models.ForeignKey(default=None, to='TWBetter.Producer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='agrospec',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='catalogs_id',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='county',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='id',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='image_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='modify_date',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='producer',
            field=models.ForeignKey(default=None, to='TWBetter.Producer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='spc_catalogs_id',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='title',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='type',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='unit_price',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='address',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='fax',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='manager',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='number',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='producer',
            name='phone',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
