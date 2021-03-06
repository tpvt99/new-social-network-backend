# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0018_auto_20170502_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='act',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_act', to='act.Act'),
        ),
        migrations.AlterField(
            model_name='status',
            name='activitiespost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_activitiespost', to='activities.ActivitiesPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='activitypost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_activitypost', to='activity.ActivityPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='actpost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_actpost', to='act.ActPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='contest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_contest', to='contest.Contest'),
        ),
        migrations.AlterField(
            model_name='status',
            name='contestpost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_contestpost', to='contest.ContestPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_event', to='event.Event'),
        ),
        migrations.AlterField(
            model_name='status',
            name='eventpost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_eventpost', to='event.EventPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='eventspost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_eventspost', to='events.EventsPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='grouppost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_grouppost', to='group.GroupPost'),
        ),
        migrations.AlterField(
            model_name='status',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_post', to='post.Post'),
        ),
        migrations.AlterField(
            model_name='status',
            name='trait',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_status_trait', to='trait.Trait'),
        ),
    ]
