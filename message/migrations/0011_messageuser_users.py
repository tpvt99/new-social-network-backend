# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-02 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0055_auto_20170520_0237'),
        ('message', '0010_messageuserinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageuser',
            name='users',
            field=models.ManyToManyField(related_name='message_messageuser_users', through='message.MessageUserInfo', to='user.User'),
        ),
    ]