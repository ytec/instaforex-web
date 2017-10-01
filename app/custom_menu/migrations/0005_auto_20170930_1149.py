# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20170929_1205'),
        ('custom_menu', '0004_auto_20170929_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_menu',
            name='page',
        ),
        migrations.AddField(
            model_name='page_menu',
            name='page',
            field=models.ForeignKey(default=1, to='pages.page'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='Pages',
            field=models.ManyToManyField(blank=True, to='custom_menu.page_menu'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='Sub_Pages',
            field=models.ManyToManyField(blank=True, to='custom_menu.Sub_Pages_menu'),
        ),
        migrations.RemoveField(
            model_name='sub_pages_menu',
            name='page',
        ),
        migrations.AddField(
            model_name='sub_pages_menu',
            name='page',
            field=models.ForeignKey(default=1, to='pages.Sub_Pages'),
        ),
    ]
