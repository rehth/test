# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('goods_info', tinymce.models.HTMLField(verbose_name='商品详情')),
            ],
            options={
                'db_table': 'goods_info',
                'verbose_name': '商品详情表',
                'verbose_name_plural': '商品详情表',
            },
        ),
    ]
