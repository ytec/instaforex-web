# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(default='Pagina', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('Imagen', models.FileField(default='Custom_Menu/img/Banner_img/default.png', upload_to='Custom_Menu/img/Banner_img')),
                ('url', models.URLField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(default='Category', max_length=50)),
                ('titel', models.CharField(default='Pagina_cms o pagina externa', max_length=100)),
                ('Level', models.CharField(default='0', max_length=3)),
                ('url', models.URLField(max_length=100, blank=True)),
                ('Banner', models.ManyToManyField(to='custom_menu.banner', blank=True)),
                ('Pages', models.ManyToManyField(to='pages.Pages', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, related_name='custom_menu_menu', to='cms.CMSPlugin', serialize=False, primary_key=True)),
                ('name', models.CharField(default='menu', max_length=50)),
                ('titel', models.CharField(default='Titulo Menu', max_length=100)),
                ('category', models.ManyToManyField(to='custom_menu.Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
