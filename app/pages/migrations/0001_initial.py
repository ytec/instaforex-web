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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Pagina')),
                ('description', models.TextField(blank=True)),
                ('titel', models.CharField(max_length=100, default='Titulo pagina ')),
                ('url', models.URLField(max_length=100, blank=True)),
                ('Level', models.CharField(max_length=3, default='1', blank=True)),
                ('page_external', models.ForeignKey(to='cms.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Pagina')),
                ('description', models.TextField(blank=True)),
                ('titel', models.CharField(max_length=100, default='Titulo pagina ')),
                ('url', models.URLField(max_length=100, blank=True)),
                ('Level', models.CharField(max_length=3, default='1', blank=True)),
                ('page_external', models.ForeignKey(to='cms.Page')),
            ],
        ),
    ]
