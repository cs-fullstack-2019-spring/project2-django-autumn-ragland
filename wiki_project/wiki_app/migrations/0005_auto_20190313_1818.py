# Generated by Django 2.0.6 on 2019-03-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_app', '0004_auto_20190313_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrtymodel',
            name='image',
            field=models.ImageField(default='images/wiki_app/static/wiki_app/images/default.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='relateditemmodel',
            name='image',
            field=models.ImageField(default='images/wiki_app/static/wiki_app/images/default.jpeg', upload_to='images'),
        ),
    ]
