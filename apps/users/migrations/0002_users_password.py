# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='\u5bc6\u7801'),
        ),
    ]
