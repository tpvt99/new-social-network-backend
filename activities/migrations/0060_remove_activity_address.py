# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-23 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0059_activity_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='address',
        ),
    ]