# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 01:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_auto_20170528_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='chat_buddies',
            new_name='chat_frames',
        ),
    ]
