# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='BonusHomePage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, to='cms.CMSPlugin', related_name='bonushome_bonushomepage', serialize=False)),
                ('name', models.CharField(default='Home', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BonusHomePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True, max_length=100)),
                ('titel', models.CharField(default='instaforex', max_length=30)),
                ('text', models.TextField(blank=True, max_length=100)),
                ('link', models.CharField(default='instaforex', max_length=100)),
                ('botton', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bonushomepage',
            name='Post',
            field=models.ManyToManyField(to='BonusHome.BonusHomePost'),
        ),
        migrations.AddField(
            model_name='bonushomepage',
            name='page',
            field=models.ForeignKey(to='cms.Page'),
        ),
    ]
