# Generated by Django 2.0.6 on 2019-03-13 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_app', '0018_auto_20190313_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrtymodel',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 20, 58, 19, 980790, tzinfo=utc), null=True),
        ),
    ]
