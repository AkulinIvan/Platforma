# Generated by Django 5.0.7 on 2025-01-15 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_request', '0004_alter_articles_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 15, 13, 30, 35, 346468), verbose_name='Дата создания заявки'),
        ),
    ]
