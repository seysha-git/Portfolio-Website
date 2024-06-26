# Generated by Django 5.0.6 on 2024-06-18 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='some string'),
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 18, 17, 7, 47, 317711, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='some string'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=75),
        ),
    ]
