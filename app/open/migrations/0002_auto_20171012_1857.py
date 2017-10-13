# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=25, default='Demo')),
            ],
        ),
        migrations.RemoveField(
            model_name='form',
            name='name',
        ),
        migrations.AddField(
            model_name='form',
            name='Form',
            field=models.ForeignKey(default=1, to='open.name'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='Form',
            field=models.ForeignKey(default=3, to='open.name'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Form',
            field=models.ForeignKey(default=2, to='open.name'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Form',
            field=models.ForeignKey(default=1, to='open.name'),
        ),
    ]
