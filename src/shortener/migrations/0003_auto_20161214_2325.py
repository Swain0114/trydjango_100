# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 23:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161213_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortener',
            old_name='activate',
            new_name='active',
        ),
    ]
