# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='language',
            field=models.BooleanField(default=1, verbose_name=True),
            preserve_default=False,
        ),
    ]
