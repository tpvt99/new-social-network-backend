# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0021_remove_status_contestpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='act',
        ),
        migrations.RemoveField(
            model_name='status',
            name='activitiespost',
        ),
        migrations.RemoveField(
            model_name='status',
            name='activitypost',
        ),
        migrations.RemoveField(
            model_name='status',
            name='actpost',
        ),
        migrations.RemoveField(
            model_name='status',
            name='eventpost',
        ),
        migrations.RemoveField(
            model_name='status',
            name='eventspost',
        ),
        migrations.RemoveField(
            model_name='status',
            name='grouppost',
        ),
        migrations.RemoveField(
            model_name='status',
            name='trait',
        ),
    ]