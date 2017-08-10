# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbnormalOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(default=django.utils.timezone.now, verbose_name='加入时间')),
                ('date_solve', models.DateTimeField(blank=True, null=True, verbose_name='解决时间')),
                ('is_solve', models.BooleanField(default=False, verbose_name='是否解决')),
            ],
            options={
                'verbose_name': '异常订单',
                'verbose_name_plural': '异常订单',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.IntegerField(choices=[(1, '挺好'), (2, '一般'), (3, '糟糕')], default=2, verbose_name='订单评价')),
                ('date_create', models.DateTimeField(blank=True, null=True, verbose_name='创建时间')),
                ('date_done', models.DateTimeField(blank=True, null=True, verbose_name='完成时间')),
                ('is_accept', models.BooleanField(default=False, verbose_name='订单是否接受')),
                ('is_done', models.BooleanField(default=False, verbose_name='订单是否完成')),
                ('is_abnormal', models.BooleanField(default=False, verbose_name='订单是否是异常订单')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Food', verbose_name='订单食物')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorder', to=settings.AUTH_USER_MODEL, verbose_name='订单发起者')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.AddField(
            model_name='abnormalorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operation.Order', verbose_name='订单'),
        ),
    ]