# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-07 08:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0017_status_timeline'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trait', '0002_auto_20170317_1815'),
        ('friend', '0004_auto_20161224_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendHeart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('heart', models.IntegerField(default=0)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_modify', models.DateTimeField(auto_now=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendheart_friend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_heart', models.IntegerField(default=0)),
                ('friend', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendrelationship_friend', to='friend.Friend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendrelationship_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='friendheart',
            name='friendrelationship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendheart_friendrelationship', to='friend.FriendRelationship'),
        ),
        migrations.AddField(
            model_name='friendheart',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendheart_status', to='status.Status'),
        ),
        migrations.AddField(
            model_name='friendheart',
            name='trait',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendheart_trait', to='trait.Trait'),
        ),
        migrations.AddField(
            model_name='friendheart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friendheart_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
