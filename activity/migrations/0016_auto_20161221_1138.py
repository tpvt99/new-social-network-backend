# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-21 11:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0015_activitymusic'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='activityparticipants',
            unique_together=set([('person', 'activity')]),
        ),
    ]