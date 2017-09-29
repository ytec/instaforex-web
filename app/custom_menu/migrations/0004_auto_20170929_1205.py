# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_menu', '0003_auto_20170928_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_menu',
            name='Sub_Pages',
        ),
        migrations.AddField(
            model_name='pages',
            name='Sub_Pages',
            field=models.ManyToManyField(to='custom_menu.Sub_Pages_menu'),
        ),
    ]
