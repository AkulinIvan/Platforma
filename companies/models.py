from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
import django_tables2 as tables

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
        
class Cities(models.Model):
    name = models.CharField('Название', max_length=50)
    status = models.BooleanField('Статус', default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["name"]),
        ]
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=Companies.Status.ENABLED)
    
class Worker(models.Model):
        
    name = models.CharField('Исполнитель', max_length=50)
    phone_number = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=18)
    type_of_worker = models.ForeignKey(Type_application, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='Специальность')
    # sms = models.BooleanField('Смс', default=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    published = PublishedManager()
    is_active = models.BooleanField('Статус', default=False)
    
    def __str__(self):
        return self.name + ' ' + "(" + str(self.type_of_worker) + ")"
    
    class Meta:
        db_table = 'worker'
        verbose_name = 'Исполнителя'
        verbose_name_plural = 'Исполнители'
        ordering = ("id",)
        
class Master(models.Model):
    name = models.CharField('Мастер', max_length=50)
    phone_number = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=18)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    published = PublishedManager()
    is_active = models.BooleanField('Статус', default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'master'
        verbose_name = 'Мастера'
        verbose_name_plural = 'Мастера'
        ordering = ("name",)
        
class Companies(models.Model):
    class Status(models.IntegerChoices):
        ENABLED = 1, "Включено"
        DISABLED = 0, "Отключено"
        
    name = models.CharField('Название компании', max_length=100)
    city = models.ForeignKey('Cities', on_delete=models.DO_NOTHING, null=True, related_name='Город')
    phone_number = PhoneNumberField('Номер телефона')
    mail = models.EmailField('E-mail', max_length=254)
    info = models.TextField('Информация', default='Не заполнено')
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='Создано')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_active = models.BooleanField('Статус', choices=Status.choices, default=Status.ENABLED)
    master = models.ForeignKey(Master, null=True, blank=True, on_delete=models.PROTECT, related_name='Мастер')
    worker = models.ManyToManyField(Worker)
    published = PublishedManager()
    objects = models.Manager()
    
    def get_absolute_url(self):
        return reverse("companies:show_company", kwargs={"company_id": self.pk})
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'companies'
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'
        ordering = ("id",)


class CompanyTable(tables.Table):
    name=tables.LinkColumn("companies:show_company", args=[tables.A("pk")])
    class Meta:
        model = Companies
        # add class="paleblue" to <table> tag
        # attrs = {'class': 'paleblue'}
