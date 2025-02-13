# Generated by Django 5.0.7 on 2025-01-21 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dezh_Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Дежурный рабочий')),
            ],
            options={
                'verbose_name': 'Дежурного исполнителя',
                'verbose_name_plural': 'Дежурные исполнители',
                'db_table': 'dezh_worker',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
                'db_table': 'roles',
                'ordering': ('id',),
                'indexes': [models.Index(fields=['role'], name='roles_role_8b02c2_idx')],
            },
        ),
        migrations.CreateModel(
            name='Status_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Статус заявки')),
                ('do', models.CharField(max_length=50, null=True, verbose_name='Действия')),
            ],
            options={
                'verbose_name': 'Статус заявки',
                'verbose_name_plural': 'Статус заявок',
                'db_table': 'status_application',
                'ordering': ('id',),
                'indexes': [models.Index(fields=['name'], name='status_appl_name_6ceb6b_idx')],
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.cities')),
            ],
            options={
                'verbose_name': 'Улицу',
                'verbose_name_plural': 'Улицы',
                'db_table': 'street',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Номер дома')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.companies')),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.master')),
                ('worker', models.ManyToManyField(to='companies.worker')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.street')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
                'db_table': 'house',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='View_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Вид заявки')),
            ],
            options={
                'verbose_name': 'Вид заявки',
                'verbose_name_plural': 'Виды заявок',
                'db_table': 'view_application',
                'ordering': ('id',),
                'indexes': [models.Index(fields=['name'], name='view_applic_name_f34571_idx')],
            },
        ),
        migrations.AddIndex(
            model_name='street',
            index=models.Index(fields=['name'], name='street_name_161986_idx'),
        ),
    ]
