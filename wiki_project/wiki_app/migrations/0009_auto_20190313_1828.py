# Generated by Django 2.0.6 on 2019-03-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki_app', '0008_auto_20190313_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrtymodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='relateditemmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]