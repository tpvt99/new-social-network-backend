# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170504_1024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name = "PostFriend",
            new_name = "PostFriendTag")
    ]