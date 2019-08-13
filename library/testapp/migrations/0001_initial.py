# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-11 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_title', models.CharField(max_length=200)),
                ('number_of_copies', models.IntegerField()),
                ('borrowed_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_id', models.IntegerField()),
                ('borrower_name', models.CharField(max_length=200)),
                ('borrower_emailid', models.EmailField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_id', models.IntegerField()),
                ('reviewer_name', models.CharField(max_length=200)),
                ('reviewer_emailid', models.EmailField(max_length=250)),
                ('reviewer_comments', models.TextField()),
            ],
        ),
    ]
