# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-31 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('mezzanine_agenda', '0030_auto_20190131_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcategory',
            name='site',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
    ]
