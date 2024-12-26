from datetime import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from companies.models import Companies



class Roles(models.Model):
    role = models.CharField('Роль', max_length=50)
    
    
    
    
    
    def __str__(self):
        return self.role
    
    class Meta:
        db_table = 'roles'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["role"]),
        ]
        
        
class Master(models.Model):
    name = models.CharField('Мастер', max_length=50)
    phone_number = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=18)
    company = models.ForeignKey(Companies, related_name='Мастера', on_delete=models.DO_NOTHING, null=True, blank=True)
    workers = models.ManyToManyField('Worker', related_name='Workers')
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='0')
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'master'
        verbose_name = 'Мастера'
        verbose_name_plural = 'Мастера'
        ordering = ("name",)


class Worker(models.Model):
    name = models.CharField('Исполнитель', max_length=50)
    type_worker = models.ForeignKey('Type_application', on_delete=models.DO_NOTHING, null=True)
    phone_number = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=18)
    company = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, null=True, related_name='Компания')
    # sms = models.BooleanField('Смс', default=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    master = models.ForeignKey(Master, related_name='Мастер', on_delete=models.DO_NOTHING, null=True, blank=True)
    # address = models.ForeignKey('House', on_delete=models.DO_NOTHING, null=True, related_name='Адрес')
    
    def __str__(self):
        return self.name 
    
    class Meta:
        db_table = 'worker'
        verbose_name = 'Исполнителя'
        verbose_name_plural = 'Исполнители'
        ordering = ("id",)


class Dezh_Worker(models.Model):
    name = models.CharField('Дежурный рабочий', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'dezh_worker'
        verbose_name = 'Дежурного исполнителя'
        verbose_name_plural = 'Дежурные исполнители'
        ordering = ("id",)
        

# class Workers(models.Model):
#     worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, null=True)
#     master = models.ForeignKey(Master, on_delete=models.DO_NOTHING, null=True)
    
#     class Meta:
#         db_table = 'workers'
#         verbose_name = 'Сотрудника'
#         verbose_name_plural = 'Сотрудники'
#         ordering = ("id",)
    
                
# class Company(models.Model):
#     name = models.CharField('Название', max_length=50)
#     city = models.ForeignKey('City', on_delete=models.DO_NOTHING, null=True)
#     phone_number = PhoneNumberField('Номер телефона 1')
#     #phone = PhoneNumberField('Номер телефона 2')
#     mail = models.EmailField('E-mail', max_length=254)
#     info = models.TextField('Информация', default='Не заполнено')
#     sms_master = models.BooleanField('Смс мастеру', default=False)
#     sms_worker = models.BooleanField('Смс исполнителю', default=False)
#     status = models.BooleanField('Статус', default=False)
#     created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    
#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'company'
#         verbose_name = 'Компанию'
#         verbose_name_plural = 'Компании'
#         ordering = ("id",)


class City(models.Model):
    name = models.CharField('Название', max_length=50)
    status = models.BooleanField('Статус', default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
        

class Street(models.Model):
    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, null=True)
    status = models.BooleanField('Статус', default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'street'
        verbose_name = 'Улицу'
        verbose_name_plural = 'Улицы'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
        

class Type_application(models.Model):
    name = models.CharField('Тип заявки', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'type_application'
        verbose_name = 'Тип заявки'
        verbose_name_plural = 'Типы заявок'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
        
        
class View_application(models.Model):
    name = models.CharField('Вид заявки', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'view_application'
        verbose_name = 'Вид заявки'
        verbose_name_plural = 'Виды заявок'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
        
class Status_application(models.Model):
    name = models.CharField('Статус заявки', max_length=50)
    do = models.CharField('Действия', max_length=50, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'status_application'
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статус заявок'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
        
        
# class Executor(models.Model):
#     name = models.ForeignKey('Usernames', on_delete=models.DO_NOTHING, null=True)
#     role = models.ForeignKey(Roles, related_name='Роль',  on_delete=models.CASCADE, default=0)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         db_table = 'executor'
#         verbose_name = 'Исполнитель'
#         verbose_name_plural = 'Исполнители'
#         ordering = ("id",)
#         indexes = [
#             models.Index(fields=["name"]),
#         ]


        
        
class Usernames(models.Model):
    FULL = 'FULL'
    ABBREVIATED = 'ABBREVIATED'
    EMPTY = 'EMPTY'
    
    CHOICES_SMS = {
        FULL: 'полный',
        ABBREVIATED: 'сокращенный',
        EMPTY: 'пусто'
    }
    
    
    name = models.CharField('Имя', max_length=55)
    phone_number = PhoneNumberField('Номер телефона', blank=True)
    mail = models.EmailField('E-mail', max_length=254, blank=True)
    role = models.ForeignKey('Roles', on_delete=models.DO_NOTHING, null=True)
    # company = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, blank=True, default=None)
    ATS = models.PositiveIntegerField('Номер АТС', blank=False, default=0)
    sms = models.CharField(max_length=55, choices=CHOICES_SMS, default=EMPTY)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'username'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
        

    

        
        
class House(models.Model):
    # ARCHIVE = 'ARH'
    # ACTIVE = 'ACT'
    
    # CHOICES_STATUS = {
    #     ARCHIVE: 'архивный',
    #     ACTIVE: 'активный',
    # }
    #abs = models.BooleanField(default=0)
    name = models.CharField('Номер дома', max_length=50)
    street = models.ForeignKey('Street', on_delete=models.DO_NOTHING, null=True)
    company = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, null=True)
    master = models.ForeignKey('Master', on_delete=models.DO_NOTHING, null=True)
    worker = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True)
    status = models.BooleanField('Статус', default=False)
    type_application = models.ForeignKey(Type_application, blank=True, on_delete=models.DO_NOTHING, null=True)
    plumbing = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Сантехника')
    electrician = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Электрика')
    carpenter = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Плотники')
    cleaners = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Уборщицы')
    wipers = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дворники')
    improvement = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Благоустройство')
    plumber_certificate = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Акт_сантехника')
    electrician_certificate = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Акт_электрика')
    networks = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Сети')
    act = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Акт')
    deratization = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дератизация')
    pest_control = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дезинсекция')
    disinfection = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дезинфекция')
    verification_of_meters = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Поверка_счетчиков')
    SOI_inspection = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Осмотр_СОИ')
    passport = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Паспортный')
    intercom_ROST = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Домофон_РОСТ')
    
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'house'
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ("id",)
        
        


