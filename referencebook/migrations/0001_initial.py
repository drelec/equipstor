# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('cartridge_name', models.CharField(max_length=20)),
                ('max_number_prints', models.IntegerField(default=0)),
                ('package', models.IntegerField(default=1)),
                ('barcode', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ColorType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('color_type', models.CharField(verbose_name='color', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Connectivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type_connectivity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaxPaperSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('max_paper_size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PrinterModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('model_name', models.CharField(max_length=50)),
                ('product_number', models.CharField(max_length=20)),
                ('model_site', models.CharField(blank=True, max_length=200)),
                ('driver_url', models.CharField(blank=True, max_length=250)),
                ('max_print_resolution_dpi', models.IntegerField(default=0)),
                ('memory_size', models.IntegerField(default=0)),
                ('max_monthly_load', models.IntegerField(default=0)),
                ('duplex_mode', models.BooleanField()),
                ('print_speed_ppm', models.IntegerField(default=0)),
                ('cartridges', models.ManyToManyField(blank=True, to='referencebook.Cartridge')),
                ('connectivity', models.ManyToManyField(to='referencebook.Connectivity')),
                ('max_paper_size', models.ForeignKey(to='referencebook.MaxPaperSize')),
            ],
        ),
        migrations.CreateModel(
            name='PrinterType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('print_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=50)),
                ('vendor_site', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='printermodel',
            name='print_type',
            field=models.ForeignKey(verbose_name='Type of print', to='referencebook.PrinterType'),
        ),
        migrations.AddField(
            model_name='printermodel',
            name='vendor_name',
            field=models.ForeignKey(to='referencebook.Vendor'),
        ),
        migrations.AddField(
            model_name='cartridge',
            name='color_type',
            field=models.ForeignKey(verbose_name='color', to='referencebook.ColorType'),
        ),
    ]
