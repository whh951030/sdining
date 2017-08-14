# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20170810_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='position',
            field=models.IntegerField(choices=[(1, '楚园食堂'), (2, '汉园食堂')], db_index=True, verbose_name='位置'),
        ),
    ]