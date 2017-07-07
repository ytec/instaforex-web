# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='SilderVarPhotos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('FilePhoto', models.FileField(default='SilderVar/img/default.png', upload_to='SilderVar/img')),
                ('url', models.URLField(blank=True, max_length=100)),
                ('titel', models.CharField(default='instaforex', max_length=100)),
                ('text', models.TextField(blank=True)),
                ('link', models.CharField(default='instaforex', max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SilderVarsPages',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, to='cms.CMSPlugin', parent_link=True, related_name='sildervar_sildervarspages', serialize=False)),
                ('name', models.CharField(default='Home', max_length=50)),
                ('Photo', models.ManyToManyField(to='SilderVar.SilderVarPhotos')),
                ('page', models.ForeignKey(to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
