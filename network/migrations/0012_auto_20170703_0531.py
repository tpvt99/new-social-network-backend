# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 05:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0011_networkchatroomuser_allow_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkchatroomuser',
            name='fetch',
        ),
        migrations.RemoveField(
            model_name='networkchatroomuser',
            name='frame',
        ),
        migrations.RemoveField(
            model_name='networkchatroomuser',
            name='read',
        ),
    ]
