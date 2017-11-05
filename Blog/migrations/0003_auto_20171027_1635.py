# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20171026_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name_url',
            field=models.CharField(default='default', max_length=45),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('programming', 'Программирование'), ('life', 'Жизнь')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]