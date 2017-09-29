# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('pages', '0002_auto_20170928_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_pages',
            name='page_external',
        ),
        migrations.AddField(
            model_name='sub_pages',
            name='page_external',
            field=models.ForeignKey(default=1, to='cms.Page'),
        ),
    ]
