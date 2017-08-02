# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Pagina')),
                ('description', models.TextField(blank=True)),
                ('Imagen', models.FileField(upload_to='Custom_Menu/img/Banner_img', default='Custom_Menu/img/Banner_img/default.png')),
                ('url', models.URLField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Category')),
                ('titel', models.CharField(max_length=100, default='Pagina_cms o pagina externa')),
                ('Level', models.CharField(max_length=3, default='0')),
                ('url', models.URLField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', parent_link=True, auto_created=True, related_name='custom_menu_menu')),
                ('name', models.CharField(max_length=50, default='menu')),
                ('titel', models.CharField(max_length=100, default='Titulo Menu')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='page_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Pagina')),
                ('Icon', models.FileField(upload_to='Custom_Menu/img', default='Custom_Menu/img/icon/default.png')),
                ('X', models.CharField(max_length=4, blank=True)),
                ('Y', models.CharField(max_length=4, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Pagina')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Pages_menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, default='Pagina')),
                ('Icon', models.FileField(upload_to='Custom_Menu/img', default='Custom_Menu/img/icon/default.png')),
                ('X', models.CharField(max_length=4, blank=True)),
                ('Y', models.CharField(max_length=4, blank=True)),
            ],
        ),
    ]
