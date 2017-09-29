# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('custom_menu', '0002_auto_20170731_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_menu',
            name='page',
        ),
        migrations.AddField(
            model_name='page_menu',
            name='page',
            field=models.ManyToManyField(to='pages.page'),
        ),
        migrations.RemoveField(
            model_name='sub_pages_menu',
            name='page',
        ),
        migrations.AddField(
            model_name='sub_pages_menu',
            name='page',
            field=models.ManyToManyField(to='pages.Sub_Pages'),
        ),
    ]
