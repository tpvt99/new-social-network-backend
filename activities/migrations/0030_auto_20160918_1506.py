# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0029_vote_can_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='can_vote',
            new_name='been_vote',
        ),
    ]