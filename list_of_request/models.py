from datetime import datetime
from django.db import models
from django.urls import reverse
from marshmallow import ValidationError
from numpy import insert
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext_lazy
import django_tables2 as tables


from companies.models import Companies, Master, Worker
from handbook.models import Dezh_Worker, House, Street, Type_application, View_application

# class CompleteApplication(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status=Articles.Status.NEW)
    
class Articles(models.Model):
        
    CURRENT = 'текущая'
    PLANNED = 'плановая'
    EMERGENCY = 'аварийная'
    DUTY = 'дежурная'
    COMMERCIAL = 'коммерческая'
    
    CHOICES_PRIORITY = (
        (CURRENT, 'текущая'),
        (PLANNED, 'плановая'),
        (EMERGENCY, 'аварийная'),
        (DUTY, 'дежурная'),
        (COMMERCIAL, 'коммерческая')
    )
    class Status(models.TextChoices):    
        NEW = "NEW", 'Новая'
        ASSIGNED = "ASSIGNED", 'Назначена'
        COMPLETED = "COMPLETED", 'Выполнена'
        CLOSED = "CLOSED", 'Закрыта'
        DELIVERED_TO_GP_TRSKK = "DELIVERED_TO_GP_TRSKK", 'Передано в ГП ЦРКК'    
        NO_POSSIBLE = "NO_POSSIBLE", "Нет возможности выполнения"
        FAILED = "FAILED", "Провалена"
        FOR_CONTRACTORS = "FOR_CONTRACTORS", 'Для подрядчиков'
        DELIVERED_IN_KRASKOM = "DELIVERED_IN_KRASKOM", 'Передано в Краском'
        DELIVERED_IN_RES = "DELIVERED_IN_RES", "Передано в РЭС"
        DELIVERED_IN_SB_RAS = "DELIVERED_IN_SB_RAS", 'Передано в СО РАН'
        DELIVERED_IN_PTO = "DELIVERED_IN_PTO", 'Передано в ПТО'

        
    
    
        
    priority = models.CharField(verbose_name='Приоритет заявки', max_length=12, choices=CHOICES_PRIORITY, default=CURRENT)
    create_time = models.DateTimeField(verbose_name='Дата создания заявки', default=datetime.now())
    street = models.ForeignKey(to=Street,  on_delete=models.PROTECT, null=True, blank=True, verbose_name="Улица")
    house = models.ForeignKey(to=House,  on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дом",) 
    flat = models.CharField('Квартира', max_length=3, null=True)
    text = models.TextField('Текст заявки', null=True, blank=True)
    phone = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=18)
    fio = models.CharField('ФИО заявителя', null=True, blank=True, max_length=255)
    job_date = models.DateField('Срок исполнения', null=True, blank=True)
    view = models.ForeignKey(to=View_application,  on_delete=models.PROTECT, verbose_name="Вид заявки", null=True, blank=True)
    type = models.ForeignKey(to=Type_application, on_delete=models.PROTECT, verbose_name="Тип заявки", null=True, blank=True)
    status = models.CharField('Статус заявки', max_length=50, choices=Status, default=Status.NEW)
    povtornaya = models.CharField("Повторная", max_length=50, null=True, blank=True, default=None)
    company = models.ForeignKey(to=Companies, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Компания", default=None)
    master = models.ForeignKey(to=Master, null=True, blank=True, verbose_name="Мастер", on_delete=models.PROTECT)
    worker = models.ForeignKey(to=Worker, null=True, blank=True, verbose_name="Исполнитель", on_delete=models.PROTECT)
    dezh_worker = models.ForeignKey(to=Dezh_Worker, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дежурный исполнитель", default=None)
    comment = models.CharField('Комментарий', max_length=50, null=True, blank=True)
    call_record = models.FileField(upload_to='call_record', blank=True, null=True, verbose_name='Запись разговора')
    voice_record = models.FileField(upload_to='voice_message', blank=True, null=True, verbose_name='Голосовые сообщения')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    new_sms = models.CharField('смс жителю "Заявка принята"', max_length=50, null=True, blank=True, default=None)
    sms_master = models.CharField('смс мастеру', max_length=50, null=True, blank=True, default=None)
    sms_about_worker = models.CharField('смс назначение исполнителя', max_length=50, null=True, blank=True, default=None)
    sms_worker = models.CharField('смс исполнителю', max_length=50, null=True, blank=True, default=None)
    sms_complete = models.CharField('смс выполнение заявки', max_length=50, null=True, blank=True, default=None)
    sms_dezh_worker = models.CharField('смс дежурному исполнителю', max_length=50, null=True, blank=True, default=None)
    materials = models.CharField('Материалы', max_length=50, null=True, blank=True)
    files = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name="Прикрепленные файлы")
    last_update = models.DateTimeField(verbose_name='Дата изменения заявки', blank=True, null=True, auto_now=True)
    converted_to_complete = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.last_update = datetime.now()
        super().save(*args, **kwargs)
        
    def display_id(self):
        return f"{datetime.now().strftime('%y')}-{self.id:06d}"
        
            
    
    
    def get_absolute_url(self):
        return reverse('list_of_request:application', kwargs={"pk": self.pk})
    
    # def __str__(self):
    #     return self.text
    
    class Meta:
        db_table = 'applications'
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["text"]),
        ]
        
    def __str__(self):
        return f"Заявка №{self.id} для {self.text}"


class ApplicationTable(tables.Table):
    '''
Таблица в которой выведены все заявки
''' 
    id=tables.LinkColumn("list_of_request:application", args=[tables.A("pk")])
    
    class Meta:
        model = Articles
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}    



# class Application_complete(models.Model):
#     create_time = models.DateTimeField(verbose_name='Дата создания заявки', default=datetime.now())
#     street = models.ForeignKey(to=Street,  on_delete=models.PROTECT, null=True, blank=True, verbose_name="Улица")
#     house = models.ForeignKey(to=House,  on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дом",) 
#     flat = models.CharField('Квартира', max_length=3, null=True)
#     text = models.TextField('Текст заявки', null=True, blank=True)
#     phone = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=18)
#     fio = models.CharField('ФИО заявителя', null=True, blank=True, max_length=255)
#     job_date = models.DateField('Срок исполнения', null=True, blank=True)
#     view = models.ForeignKey(to=View_application,  on_delete=models.PROTECT, verbose_name="Вид заявки", null=True, blank=True)
#     type = models.ForeignKey(to=Type_application, on_delete=models.PROTECT, verbose_name="Тип заявки", null=True, blank=True)
#     status = models.CharField(verbose_name='Статус заявки', max_length=50)
#     povtornaya = models.CharField("Повторная", max_length=50, null=True, blank=True, default=None)
#     company = models.ForeignKey(to=Companies, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Компания", default=None)
#     master = models.ForeignKey(to=Master, null=True, blank=True, verbose_name="Мастер", on_delete=models.PROTECT)
#     worker = models.ForeignKey(to=Worker, null=True, blank=True, verbose_name="Исполнитель", on_delete=models.PROTECT)
#     dezh_worker = models.ForeignKey(to=Dezh_Worker, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дежурный исполнитель", default=None)
#     comment = models.CharField('Комментарий', max_length=50, null=True, blank=True)
#     call_record = models.FileField(upload_to='call_record', blank=True, null=True, verbose_name='Запись разговора')
#     voice_record = models.FileField(upload_to='voice_message', blank=True, null=True, verbose_name='Голосовые сообщения')
#     user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
#     new_sms = models.CharField('смс жителю "Заявка принята"', max_length=50, null=True, blank=True, default=None)
#     sms_master = models.CharField('смс мастеру', max_length=50, null=True, blank=True, default=None)
#     sms_about_worker = models.CharField('смс назначение исполнителя', max_length=50, null=True, blank=True, default=None)
#     sms_worker = models.CharField('смс исполнителю', max_length=50, null=True, blank=True, default=None)
#     sms_complete = models.CharField('смс выполнение заявки', max_length=50, null=True, blank=True, default=None)
#     sms_dezh_worker = models.CharField('смс дежурному исполнителю', max_length=50, null=True, blank=True, default=None)
#     materials = models.CharField('Материалы', max_length=50, null=True, blank=True)
#     files = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name="Прикрепленные файлы")
#     last_update = models.DateTimeField(verbose_name='Дата изменения заявки', blank=True, null=True, auto_now=True)
#     converted_to_open = models.BooleanField(default=True)
    
#     class Meta:
#         db_table = 'application_complete'
#         verbose_name = 'Выполненную заявку'
#         verbose_name_plural = 'Выполненные заявки'
#         ordering = ("id",)
#         indexes = [
#             models.Index(fields=["text"]),
#         ]
    
#     def get_absolute_urll(self):
#         return reverse('list_of_request:detail_complete_application', kwargs={"pk": self.pk})
        
    
    
    
    
    
    
    
    

    
    

    
    
    
    
    
    
    
    

        
