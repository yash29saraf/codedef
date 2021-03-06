# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-10 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googform', '0005_auto_20161109_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='knowledge',
            name='topics',
        ),
        migrations.AddField(
            model_name='knowledge',
            name='topics',
            field=models.ManyToManyField(to='googform.Topics'),
        ),
    ]
