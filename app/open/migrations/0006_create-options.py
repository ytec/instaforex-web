# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open', '0003_auto_20171012_1922'),
    ]

    operations = [
        migrations.RunSQL("DELETE FROM open_name;"),
        migrations.RunSQL("INSERT INTO open_name (name) VALUES ('Real');"),
        migrations.RunSQL("INSERT INTO open_name (name) VALUES ('Demo');"),
        migrations.RunSQL("INSERT INTO open_name (name) VALUES ('Anonymous');"),
        ]
