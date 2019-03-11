# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 16:06
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_cms', '0015_countriesindex_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casestudy',
            name='app_instance',
        ),
        migrations.RemoveField(
            model_name='casestudy',
            name='category',
        ),
        migrations.AddField(
            model_name='country',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='cartoview_cms.ContentCategory'),
        ),
    ]
