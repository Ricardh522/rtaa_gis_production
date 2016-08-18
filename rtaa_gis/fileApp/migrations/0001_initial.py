# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_name', models.CharField(max_length=50, null=True)),
                ('date_assigned', models.DateField(auto_now_add=True, null=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ('grid_cell', 'file', 'date_assigned', 'comment'),
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(max_length=255, unique=True)),
                ('base_name', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=25)),
                ('mime', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=25)),
                ('date_added', models.DateField(auto_now=True)),
                ('comment', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ('base_name',),
            },
        ),
        migrations.CreateModel(
            name='GridCell',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='filemodel',
            name='grid_cells',
            field=models.ManyToManyField(through='fileApp.Assignment', to='fileApp.GridCell'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileApp.FileModel'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='grid_cell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileApp.GridCell'),
        ),
    ]
