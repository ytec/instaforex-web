# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open', '0007_auto_20171120_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openaccountreal',
            name='Direcc2',
            field=models.CharField(max_length=100, blank=True, default='Direcc2'),
        ),
        migrations.AlterField(
            model_name='openaccountreal',
            name='NotificationLanguage',
            field=models.CharField(max_length=30, blank=True, default='EN'),
        ),
    ]
