# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 18:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20170625_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
