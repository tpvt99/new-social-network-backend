# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_messageuser_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageuser',
            name='message_type',
            field=models.CharField(default='user', max_length=10),
        ),
    ]