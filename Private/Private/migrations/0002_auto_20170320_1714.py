# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 17:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Private', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, null=True)),
                ('mob_no', models.IntegerField(null=True)),
                ('email', models.TextField(null=True)),
                ('password', models.TextField(max_length=8, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
