# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback', '0008_auto_20170401_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashback',
            old_name='wxname',
            new_name='wechat',
        ),
        migrations.AddField(
            model_name='cashback',
            name='alipay',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='会员支付宝账号'),
        ),
    ]
