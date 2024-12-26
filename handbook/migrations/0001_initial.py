# Generated by Django 5.0.7 on 2024-12-25 06:25

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'city',
                'ordering': ('id',),
                'indexes': [models.Index(fields=['name'], name='city_name_88111b_idx')],
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
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.city')),
            ],
            options={
                'verbose_name': 'Улицу',
                'verbose_name_plural': 'Улицы',
                'db_table': 'street',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Type_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип заявки')),
            ],
            options={
                'verbose_name': 'Тип заявки',
                'verbose_name_plural': 'Типы заявок',
                'db_table': 'type_application',
                'ordering': ('id',),
                'indexes': [models.Index(fields=['name'], name='type_applic_name_6a2720_idx')],
            },
        ),
        migrations.CreateModel(
            name='Usernames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Номер телефона')),
                ('mail', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('ATS', models.PositiveIntegerField(default=0, verbose_name='Номер АТС')),
                ('sms', models.CharField(choices=[('FULL', 'полный'), ('ABBREVIATED', 'сокращенный'), ('EMPTY', 'пусто')], default='EMPTY', max_length=55)),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.roles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'username',
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
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Исполнитель')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=18, null=True, region=None, verbose_name='Номер телефона')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Компания', to='companies.companies')),
                ('type_worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.type_application')),
                ('user', models.OneToOneField(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Исполнителя',
                'verbose_name_plural': 'Исполнители',
                'db_table': 'worker',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Мастер')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=18, null=True, region=None, verbose_name='Номер телефона')),
                ('company', models.ForeignKey(default='Не назначено', on_delete=django.db.models.deletion.DO_NOTHING, related_name='Мастера', to='companies.companies')),
                ('user', models.OneToOneField(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('workers', models.ManyToManyField(to='handbook.worker')),
            ],
            options={
                'verbose_name': 'Мастера',
                'verbose_name_plural': 'Мастера',
                'db_table': 'master',
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
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.master')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.street')),
                ('type_application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.type_application')),
                ('SOI_inspection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Осмотр_СОИ', to='handbook.worker')),
                ('act', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Акт', to='handbook.worker')),
                ('carpenter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Плотники', to='handbook.worker')),
                ('cleaners', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Уборщицы', to='handbook.worker')),
                ('deratization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Дератизация', to='handbook.worker')),
                ('disinfection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Дезинфекция', to='handbook.worker')),
                ('electrician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Электрика', to='handbook.worker')),
                ('electrician_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Акт_электрика', to='handbook.worker')),
                ('improvement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Благоустройство', to='handbook.worker')),
                ('intercom_ROST', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Домофон_РОСТ', to='handbook.worker')),
                ('networks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Сети', to='handbook.worker')),
                ('passport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Паспортный', to='handbook.worker')),
                ('pest_control', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Дезинсекция', to='handbook.worker')),
                ('plumber_certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Акт_сантехника', to='handbook.worker')),
                ('plumbing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Сантехника', to='handbook.worker')),
                ('verification_of_meters', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Поверка_счетчиков', to='handbook.worker')),
                ('wipers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Дворники', to='handbook.worker')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='handbook.worker')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
                'db_table': 'house',
                'ordering': ('id',),
            },
        ),
        migrations.AddIndex(
            model_name='street',
            index=models.Index(fields=['name'], name='street_name_161986_idx'),
        ),
        migrations.AddIndex(
            model_name='usernames',
            index=models.Index(fields=['name'], name='username_name_b6298b_idx'),
        ),
    ]
