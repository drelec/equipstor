# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referencebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('page_counter', models.IntegerField(default=0, blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(default='', blank=True, max_length=250)),
                ('barcode', models.CharField(blank=True, max_length=20)),
                ('model_name', models.ForeignKey(to='referencebook.PrinterModel')),
            ],
        ),
    ]
