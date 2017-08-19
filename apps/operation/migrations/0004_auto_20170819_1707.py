# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-19 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20170819_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercollect',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mycollect', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]