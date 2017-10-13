# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open', '0002_auto_20171012_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Form',
            field=models.ForeignKey(default=2, to='open.name'),
        ),
    ]
