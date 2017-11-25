# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('open', '0006_create-options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openaccountanonymous',
            name='Form',
        ),
        migrations.RemoveField(
            model_name='openaccountdemo',
            name='Form',
        ),
        migrations.RemoveField(
            model_name='openaccountreal',
            name='Form',
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='City',
            field=models.CharField(max_length=30, default='City'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='Direcc',
            field=models.CharField(max_length=100, default='Direcc'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='Direcc2',
            field=models.CharField(max_length=100, default='Direcc2'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='Email',
            field=models.EmailField(max_length=254, default='example@example.com'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='Name',
            field=models.CharField(max_length=25, default='Name'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='Phone',
            field=models.CharField(max_length=15, default='Phone'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='SurNames',
            field=models.CharField(max_length=100, default='SurName'),
        ),
        migrations.AddField(
            model_name='openaccountanonymous',
            name='ZipCode',
            field=models.CharField(max_length=10, default='ZipCode'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='AccountType',
            field=models.CharField(max_length=30, default='AccountType'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='AffiliateCode',
            field=models.CharField(max_length=10, default='1234'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='City',
            field=models.CharField(max_length=30, default='City'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Country',
            field=models.CharField(max_length=30, default='Country'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Currency',
            field=models.CharField(max_length=30, default='Currency'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='DateOfBirth',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Direcc',
            field=models.CharField(max_length=100, default='Direcc'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Direcc2',
            field=models.CharField(max_length=100, default='Direcc2'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Email',
            field=models.EmailField(max_length=254, default='example@example.com'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='InitialDeposit',
            field=models.CharField(max_length=20, default='1000'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='InvestorPassword',
            field=models.CharField(max_length=30, default='password'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Language',
            field=models.CharField(max_length=10, default='En'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Leverage',
            field=models.CharField(max_length=30, default='Leverage'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Name',
            field=models.CharField(max_length=25, default='Name'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='NotificationLanguage',
            field=models.CharField(max_length=30, default='AccountType'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='Phone',
            field=models.CharField(max_length=15, default='Phone'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='State',
            field=models.CharField(max_length=30, default='State'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='SurNames',
            field=models.CharField(max_length=100, default='SurName'),
        ),
        migrations.AddField(
            model_name='openaccountdemo',
            name='ZipCode',
            field=models.CharField(max_length=10, default='ZipCode'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='AccountType',
            field=models.CharField(max_length=30, default='AccountType'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='AffiliateCode',
            field=models.CharField(max_length=10, default='1234'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='City',
            field=models.CharField(max_length=30, default='City'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Country',
            field=models.CharField(max_length=30, default='Country'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Currency',
            field=models.CharField(max_length=30, default='Currency'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='DateOfBirth',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Direcc',
            field=models.CharField(max_length=100, default='Direcc'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Direcc2',
            field=models.CharField(max_length=100, default='Direcc2'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Email',
            field=models.EmailField(max_length=254, default='example@example.com'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Language',
            field=models.CharField(max_length=10, default='En'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Leverage',
            field=models.CharField(max_length=30, default='Leverage'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Name',
            field=models.CharField(max_length=25, default='Name'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='NotificationLanguage',
            field=models.CharField(max_length=30, default='AccountType'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='Phone',
            field=models.CharField(max_length=15, default='Phone'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='State',
            field=models.CharField(max_length=30, default='State'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='SurNames',
            field=models.CharField(max_length=100, default='SurName'),
        ),
        migrations.AddField(
            model_name='openaccountreal',
            name='ZipCode',
            field=models.CharField(max_length=10, default='ZipCode'),
        ),
    ]
