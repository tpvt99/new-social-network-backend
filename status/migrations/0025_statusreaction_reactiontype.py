# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0024_statusreaction_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusreaction',
            name='reactionType',
            field=models.IntegerField(null=True),
        ),
    ]
