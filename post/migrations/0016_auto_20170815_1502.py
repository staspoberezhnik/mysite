# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 12:02
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_auto_20170811_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]