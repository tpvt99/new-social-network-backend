# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0023_auto_20170115_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPostFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='activitypost',
            name='private',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitypostfriend',
            name='activitypost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activitypostfriend_activitypost', to='activity.ActivityPost'),
        ),
        migrations.AddField(
            model_name='activitypostfriend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activitypostfriend_friend', to=settings.AUTH_USER_MODEL),
        ),
    ]