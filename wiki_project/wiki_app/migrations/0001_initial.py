# Generated by Django 2.0.6 on 2019-03-12 17:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrtyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=500)),
                ('text', models.TextField(default='')),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RelatedItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=500)),
                ('text', models.TextField(default='')),
                ('image', models.CharField(default='', max_length=500)),
                ('entry_model_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki_app.EnrtyModel')),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('password', models.CharField(default='', max_length=500)),
                ('email', models.EmailField(default='', max_length=254)),
                ('user_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='enrtymodel',
            name='user_model_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki_app.UserModel'),
        ),
    ]