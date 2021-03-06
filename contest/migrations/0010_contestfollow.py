# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0009_auto_20170108_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_contestfollow_contest', to='contest.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_contestfollow_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
