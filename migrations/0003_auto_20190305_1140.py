# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_cms', '0002_staticpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindex',
            options={'verbose_name': 'Blog'},
        ),
        migrations.AlterModelOptions(
            name='newsindex',
            options={'verbose_name': 'News'},
        ),
    ]