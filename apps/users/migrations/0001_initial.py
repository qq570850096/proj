# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-16 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u7528\u6237\u540d')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
            },
        ),
    ]