# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0006_auto_20170131_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyagedates',
            name='arrival_at_second_place_landing',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date of arrival at second place of landing (DATARR37,36,38)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='date_departed_africa',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date vessel departed Africa (DATELEFTAFR)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='departure_last_place_of_landing',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date of departure from last place of landing (DDEPAMB,*,C)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='first_dis_of_slaves',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date of first disembarkation of slaves (DATARR33,32,34)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='imp_arrival_at_port_of_dis',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Year of arrival at port of disembarkation (YEARAM)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='imp_departed_africa',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Year departed Africa'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='imp_voyage_began',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Year voyage began'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='slave_purchase_began',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date that slave purchase began (D1SLATRB,A,C)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='third_dis_of_slaves',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date of third disembarkation of slaves (DATARR40,39,41)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='vessel_left_port',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date that vessel left last slaving port (DLSLATRB,A,C)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='voyage_began',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date that voyage began (DATEDEPB,A,C)'),
        ),
        migrations.AlterField(
            model_name='voyagedates',
            name='voyage_completed',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile(b'^(\\d{1,2}|),(\\d{1,2}|),(\\d{4}|)$'), message=b'Please type a date in the format MM,DD,YYYY (individual entries may be blank)', code=b'invalid')], max_length=10, blank=True, help_text=b'Date in format: MM,DD,YYYY', null=True, verbose_name=b'Date on which slave voyage completed (DATARR44,43,45)'),
        ),
    ]
