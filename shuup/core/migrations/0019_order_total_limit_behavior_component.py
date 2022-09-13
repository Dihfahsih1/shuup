# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-06 05:27
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import shuup.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0018_visibility_defaults'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTotalLimitBehaviorComponent',
            fields=[
                ('servicebehaviorcomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shuup.ServiceBehaviorComponent')),
                ('min_price_value', shuup.core.fields.MoneyValueField(blank=True, decimal_places=9, max_digits=36, null=True)),
                ('max_price_value', shuup.core.fields.MoneyValueField(blank=True, decimal_places=9, max_digits=36, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('shuup.servicebehaviorcomponent',),
        ),
    ]
