# Generated by Django 2.0.6 on 2019-03-13 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_app', '0013_auto_20190313_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrtymodel',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
