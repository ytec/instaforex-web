# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('custom_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_pages_menu',
            name='page',
            field=models.ForeignKey(to='pages.Sub_Pages'),
        ),
        migrations.AddField(
            model_name='pages',
            name='Pages',
            field=models.ManyToManyField(to='custom_menu.page_menu'),
        ),
        migrations.AddField(
            model_name='page_menu',
            name='Sub_Pages',
            field=models.ManyToManyField(to='custom_menu.Sub_Pages_menu'),
        ),
        migrations.AddField(
            model_name='page_menu',
            name='page',
            field=models.ForeignKey(to='pages.page'),
        ),
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.ManyToManyField(to='custom_menu.Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='Banner',
            field=models.ManyToManyField(to='custom_menu.banner', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='Pages',
            field=models.ManyToManyField(to='custom_menu.Pages', blank=True),
        ),
    ]
