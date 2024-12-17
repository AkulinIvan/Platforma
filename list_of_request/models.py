from datetime import datetime
from django.db import models
from django.urls import reverse
from marshmallow import ValidationError
from numpy import insert
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext_lazy

from handbook.models import Company, Dezh_Worker, House, Master, Street, Type_application, View_application, Worker

class Articles(models.Model):
    
    ACTIVE = 'ACTIVE'
    ARCHIVE = 'ARCHIVE'
    
    CHOICES_RECORD = {
        ACTIVE: 'активная',
        ARCHIVE: 'архивная'
    }
    def status_validator(application_status):
        if application_status not in ["Открытая", "Закрытая", "Выполняется", "Нужно уточнение"]:
            raise ValidationError(
                gettext_lazy('%(application_status) неправильный статус заявки'),
                params={'application_status': application_status},
            )
    
    create_time = models.DateTimeField(verbose_name='Дата создания заявки', default=datetime.now())
    date_from = models.DateField('Дата от', null=True, blank=True)
    date_to = models.DateField('Дата до', null=True, blank=True)
    time_from = models.TimeField('Время от', null=True, blank=True)
    time_to = models.TimeField('Время до', null=True, blank=True)
    date = models.DateField('Дата', null=True, blank=True)
    clock = models.TimeField('Время', null=True, blank=True)
    street = models.ForeignKey(to=Street,  on_delete=models.PROTECT, null=True, blank=True, verbose_name="Улица")
    house = models.ForeignKey(to=House,  on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дом",) 
    flat = models.CharField('Квартира', max_length=3, null=True)
    text = models.TextField('Текст заявки', null=True, blank=True, max_length=255)
    phone = PhoneNumberField('Номер телефона', null=True, blank=True, max_length=12)
    extension_phone = models.CharField('Доп. телефон', max_length=50, default='Не указан номер')
    fio = models.CharField('ФИО заявителя', null=True, blank=True, max_length=50)
    job_date = models.DateField('Срок исполнения', null=True, blank=True)
    view = models.ForeignKey(to=View_application,  on_delete=models.PROTECT, verbose_name="Вид заявки", null=True, blank=True)
    type = models.ForeignKey(to=Type_application, on_delete=models.PROTECT, verbose_name="Тип заявки", null=True, blank=True)
    application_status = models.CharField(verbose_name='Статус заявки', max_length=50, validators=[status_validator], default=[0])
    povtornaya = models.CharField("Повторная", max_length=50, null=True, blank=True, default=None)
    company = models.ForeignKey(to=Company, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Компания", default=None)
    master = models.ForeignKey(to=Master, null=True, blank=True, verbose_name="Мастер", on_delete=models.PROTECT)
    worker = models.ForeignKey(to=Worker, null=True, blank=True, verbose_name="Исполнитель", on_delete=models.PROTECT)
    dezh_worker = models.ForeignKey(to=Dezh_Worker, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Дежурный исполнитель", default=None)
    comment = models.CharField('Комментарий', max_length=50, null=True, blank=True)
    end_date = models.DateField('Дата выполнения', max_length=50, null=True, blank=True)
    call_record = models.FileField(upload_to='call_record', blank=True, null=True, verbose_name='Запись разговора')
    voice_record = models.FileField(upload_to='voice_message', blank=True, null=True, verbose_name='Голосовые сообщения')
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, null=True, blank=True)
    record_status = models.CharField(verbose_name='Статус записи', max_length=55, choices=CHOICES_RECORD, default=ACTIVE)
    new_sms = models.CharField('смс жителю "Заявка принята"', max_length=50, null=True, blank=True, default=None)
    sms_master = models.CharField('смс мастеру', max_length=50, null=True, blank=True, default=None)
    sms_about_worker = models.CharField('смс назначение исполнителя', max_length=50, null=True, blank=True, default=None)
    sms_worker = models.CharField('смс исполнителю', max_length=50, null=True, blank=True, default=None)
    sms_complete = models.CharField('смс выполнение заявки', max_length=50, null=True, blank=True, default=None)
    sms_dezh_worker = models.CharField('смс дежурному исполнителю', max_length=50, null=True, blank=True, default=None)
    materials = models.CharField('Материалы', max_length=50, null=True, blank=True)
    files = models.ImageField(upload_to='photo', blank=True, null=True, verbose_name="Прикрепленные файлы")
    last_update = models.DateTimeField(verbose_name='Дата изменения заявки', blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        self.last_update = datetime.now()
        super().save(*args, **kwargs)
        
    def display_id(self):
        return f"{datetime.now().strftime('%y')}-{self.id:06d}"
        
            
    
    
    def get_absolute_url(self):
        return reverse('list_of_request:application', kwargs={"application_id": self.pk})
    
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
        return f"{self.phone}: {self.text}"
    
    
    
    
    
    
    
    

    
    

    
    
    
    
    
    
    
    

        
