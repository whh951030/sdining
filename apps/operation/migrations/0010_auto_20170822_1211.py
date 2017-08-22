# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0009_ordertextcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertextcomment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operation.Order', verbose_name='订单'),
        ),
    ]
