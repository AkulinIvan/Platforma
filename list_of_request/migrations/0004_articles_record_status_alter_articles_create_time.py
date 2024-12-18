# Generated by Django 5.0.7 on 2024-12-17 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_of_request', '0003_remove_articles_record_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='record_status',
            field=models.CharField(choices=[('активная', 'активная'), ('архивная', 'архивная')], default='активная', max_length=55, verbose_name='Статус записи'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 17, 14, 3, 31, 9712), verbose_name='Дата создания заявки'),
        ),
    ]
