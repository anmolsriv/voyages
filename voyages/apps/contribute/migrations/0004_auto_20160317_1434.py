# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 18:34
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contribute', '0003_interimpreexistingsource'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRequest',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('contribution_id', models.TextField()),
                ('email_sent', models.BooleanField(default=False)),
                ('response', models.IntegerField(default=0)),
                ('editor_comments', models.TextField()),
                ('reviewer_comments', models.TextField(null=True)),
                ('final_decision', models.IntegerField(default=0)),
                ('archived', models.BooleanField(default=False)),
                ('editor',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
                ('suggested_reviewer',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='+',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewVoyageContribution',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('notes',
                 models.TextField(help_text=b'Reviewer notes',
                                  max_length=10000,
                                  verbose_name=b'Notes')),
                ('request',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='contribute.ReviewRequest')),
                ('review_interim_voyage',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='+',
                                   to='contribute.InterimVoyage')),
            ],
        ),
        migrations.AddField(
            model_name='deletevoyagecontribution',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True,
                                       default=datetime.datetime(2016,
                                                                 3,
                                                                 17,
                                                                 18,
                                                                 34,
                                                                 22,
                                                                 655793,
                                                                 tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='editvoyagecontribution',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True,
                                       default=datetime.datetime(2016,
                                                                 3,
                                                                 17,
                                                                 18,
                                                                 34,
                                                                 26,
                                                                 700226,
                                                                 tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mergevoyagescontribution',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True,
                                       default=datetime.datetime(2016,
                                                                 3,
                                                                 17,
                                                                 18,
                                                                 34,
                                                                 27,
                                                                 834342,
                                                                 tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newvoyagecontribution',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True,
                                       default=datetime.datetime(2016,
                                                                 3,
                                                                 17,
                                                                 18,
                                                                 34,
                                                                 28,
                                                                 643610,
                                                                 tzinfo=utc)),
            preserve_default=False,
        ),
    ]
