# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocorate', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='chocolate',
            name='picture_alt',
            field=models.CharField(default='some image should be here', max_length=200),
        ),
    ]