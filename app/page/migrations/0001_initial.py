# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(default='Pagina', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('titel', models.CharField(default='Titulo pagina ', max_length=100)),
                ('url', models.URLField(max_length=100, blank=True)),
                ('Icon', models.FileField(default='Custom_Menu/img/icon/default.png', upload_to='Custom_Menu/img')),
                ('X', models.CharField(max_length=4, blank=True)),
                ('Y', models.CharField(max_length=4, blank=True)),
                ('Level', models.CharField(default='1', max_length=3, blank=True)),
                ('page_external', models.ForeignKey(to='cms.Page')),
            ],
        ),
    ]
