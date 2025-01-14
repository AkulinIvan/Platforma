
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _
from companies.models import Cities, Companies, Master, PublishedManager, Type_application, Worker



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
        
        


class Dezh_Worker(models.Model):
    name = models.CharField('Дежурный рабочий', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'dezh_worker'
        verbose_name = 'Дежурного исполнителя'
        verbose_name_plural = 'Дежурные исполнители'
        ordering = ("id",)
        

class Street(models.Model):
    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey(to=Cities, on_delete=models.DO_NOTHING, null=True)
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
    master = models.ForeignKey(Master, on_delete=models.DO_NOTHING, null=True)
    worker = models.ManyToManyField(Worker)
    status = models.BooleanField('Статус', default=False)
    
    # plumbing = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Сантехника')
    # electrician = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Электрика')
    # carpenter = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Плотники')
    # cleaners = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Уборщицы')
    # wipers = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дворники')
    # improvement = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Благоустройство')
    # plumber_certificate = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Акт_сантехника')
    # electrician_certificate = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Акт_электрика')
    # networks = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Сети')
    # act = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Акт')
    # deratization = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дератизация')
    # pest_control = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дезинсекция')
    # disinfection = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Дезинфекция')
    # verification_of_meters = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Поверка_счетчиков')
    # SOI_inspection = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Осмотр_СОИ')
    # passport = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Паспортный')
    # intercom_ROST = models.ForeignKey('Worker', blank=True, on_delete=models.DO_NOTHING, null=True, related_name='Домофон_РОСТ')
    
    
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'house'
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ("id",)
        
        


