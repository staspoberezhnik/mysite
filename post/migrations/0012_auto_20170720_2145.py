# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_post_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
