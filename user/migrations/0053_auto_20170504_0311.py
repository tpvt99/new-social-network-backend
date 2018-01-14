# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0052_auto_20170504_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]