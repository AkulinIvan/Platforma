# Generated by Django 5.0.7 on 2024-12-26 06:52

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_companies_sms_master_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='companies',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
