# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noti', '0052_auto_20170519_0248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusanotification',
            old_name='who_vote',
            new_name='user',
        ),
    ]
