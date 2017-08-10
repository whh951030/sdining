# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 10:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_oauthqq'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauthqq',
            name='nickname',
            field=models.CharField(blank=True, max_length=256, verbose_name='昵称'),
        ),
        migrations.AddField(
            model_name='oauthqq',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '未知')], default=3, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='oauthqq',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]