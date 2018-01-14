# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 01:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0016_auto_20161221_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='activityspam',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='activityspam',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='activityspam',
            name='user',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='spam',
            new_name='report',
        ),
        migrations.DeleteModel(
            name='ActivitySpam',
        ),
        migrations.AddField(
            model_name='activityreport',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activityreport_activity', to='activity.Activity'),
        ),
        migrations.AddField(
            model_name='activityreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_activityreport_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='activityreport',
            unique_together=set([('activity', 'user')]),
        ),
    ]