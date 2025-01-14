# Generated by Django 5.0.7 on 2025-01-14 01:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_request', '0002_alter_articles_create_time'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='articles',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='converted_to_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='articles',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 14, 8, 47, 6, 364453), verbose_name='Дата создания заявки'),
        ),
    ]
