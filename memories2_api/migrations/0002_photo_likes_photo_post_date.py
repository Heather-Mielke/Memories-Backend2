# Generated by Django 4.0.3 on 2022-04-01 20:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories2_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo',
            name='post_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]