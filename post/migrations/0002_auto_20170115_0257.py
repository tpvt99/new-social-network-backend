# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='province',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='province_unicode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]
