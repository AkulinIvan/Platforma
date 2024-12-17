from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from handbook.models import Company, Roles

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    role = models.ForeignKey(to=Roles, null=True, blank=True, verbose_name="Роль", default=None, on_delete=models.PROTECT)
    phone = PhoneNumberField('Номер телефона', max_length=50, default='Не указан номер')
    company = models.ForeignKey(to=Company, null=True, blank=True, verbose_name="Компания", default=None, on_delete=models.PROTECT)
    nomer_АТС = models.IntegerField('Номер АТС', null=True)
    
    class Meta:
        db_table = 'userprofile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ("phone",)
        indexes = [
            models.Index(fields=["user"]),
        ]
    
