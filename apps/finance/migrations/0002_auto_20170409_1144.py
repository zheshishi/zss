# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 11:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fwalletbill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='forder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='faccounttransferaudits',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL, verbose_name='审核人'),
        ),
        migrations.AddField(
            model_name='faccounttransferaudits',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL, verbose_name='申请人'),
        ),
    ]