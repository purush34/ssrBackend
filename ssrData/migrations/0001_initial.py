# Generated by Django 3.1 on 2022-11-21 01:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2022)])),
                ('mentor', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]