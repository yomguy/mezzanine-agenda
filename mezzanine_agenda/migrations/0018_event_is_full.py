# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-21 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0017_auto_20170222_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_full',
            field=models.BooleanField(default=False, verbose_name='Is full'),
        ),
    ]
