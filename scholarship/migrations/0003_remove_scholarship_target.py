# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-02 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0002_scholarshiptarget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='target',
        ),
    ]
