from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# from handbook.models import Master, Worker


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
        return super().get_queryset().filter(is_active=1)
        
class Companies(models.Model):
    name = models.CharField('Название', max_length=50)
    city = models.ForeignKey('Cities', on_delete=models.DO_NOTHING, null=True, related_name='Город')
    phone_number = PhoneNumberField('Номер телефона')
    mail = models.EmailField('E-mail', max_length=254)
    info = models.TextField('Информация', default='Не заполнено')
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='Создано')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_active = models.BooleanField('Статус', default=False)
    # master = models.ManyToManyField(Master)
    # worker = models.ManyToManyField(Worker)
    members = models.ManyToManyField(User)
    published = PublishedManager()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'companies'
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'
        ordering = ("id",)
