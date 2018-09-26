# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-18 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_agenda', '0026_auto_20170823_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-start', 'rank'), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='eventprice',
            options={'ordering': ('-value',), 'verbose_name': 'Event price', 'verbose_name_plural': 'Event prices'},
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.CharField(blank=True, default='', help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventlocation',
            name='slug',
            field=models.CharField(blank=True, default='', help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, verbose_name='URL'),
            preserve_default=False,
        ),
    ]