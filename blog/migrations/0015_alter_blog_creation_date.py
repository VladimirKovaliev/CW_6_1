# Generated by Django 4.2.7 on 2024-01-15 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_blog_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 19, 57, 46, 636563), verbose_name='Дата создания'),
        ),
    ]
