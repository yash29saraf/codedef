# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googform', '0002_knowledge_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge',
            name='language',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='topics',
            field=models.CharField(choices=[('Searching', 'Searching'), ('Sorting', 'Sorting'), ('DP', 'DP')], max_length=100),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='year',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100),
        ),
    ]
