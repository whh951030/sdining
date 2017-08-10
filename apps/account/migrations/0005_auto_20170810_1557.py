# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 15:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthQQProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qq_openid', models.CharField(max_length=64)),
                ('nickname', models.CharField(blank=True, max_length=256, verbose_name='昵称')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '未知')], default=1, verbose_name='性别')),
                ('stuid', models.CharField(max_length=20, verbose_name='学号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.RemoveField(
            model_name='oauthqq',
            name='user',
        ),
        migrations.DeleteModel(
            name='OAuthQQ',
        ),
    ]
