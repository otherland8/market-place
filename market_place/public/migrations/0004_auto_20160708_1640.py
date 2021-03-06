# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_auto_20160629_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
        migrations.RemoveField(
            model_name='article',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='article',
            name='sold',
        ),
        migrations.AddField(
            model_name='article',
            name='buyout_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='article',
            name='expire_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='starting_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
