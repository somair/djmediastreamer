# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-06 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djmediastreamer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djmediastreamer', '0006_usersettings_vp8_crf'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubtitlesFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField()),
                ('directory', models.TextField()),
                ('extension', models.CharField(max_length=5)),
                ('language', models.TextField(blank=True, null=True)),
                ('mediafile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djmediastreamer.MediaFile')),
            ],
        ),
        migrations.CreateModel(
            name='SubtitlesLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(db_index=True)),
                ('start', models.TimeField(db_index=True)),
                ('end', models.TimeField(db_index=True)),
                ('text', models.TextField()),
                ('text_vector', djmediastreamer.fields.TsVectorField(blank=True, null=True)),
                ('subtitlefile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djmediastreamer.SubtitlesFile')),
            ],
        ),
    ]
