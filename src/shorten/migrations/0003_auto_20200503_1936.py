# Generated by Django 2.2.12 on 2020-05-03 19:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_auto_20200503_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='redirect_count',
            field=models.IntegerField(default=0, help_text='Number of times shortcode has been retreived'),
        ),
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(help_text='url shortname', max_length=6, unique=True, validators=[django.core.validators.RegexValidator(code='invalid shortcode', message='shortcode must be lowercase alpha numeric charater; underscore is allowed.', regex='^[a-z0-9_]{6}')], verbose_name='shorcode'),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='url'),
        ),
    ]
