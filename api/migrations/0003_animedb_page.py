# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170217_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='animedb',
            name='page',
            field=models.CharField(default=1, max_length=500, verbose_name='ページ'),
        ),
    ]
