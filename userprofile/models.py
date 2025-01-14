from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from handbook.models import Roles


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, null=True, blank=True, verbose_name="Роль", default=None, on_delete=models.PROTECT)
    phone = PhoneNumberField('Номер телефона', max_length=50, default='Не указан номер')
    nomer_ATS = models.IntegerField('Номер АТС', null=True)
    
    class Meta:
        db_table = 'userprofile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ("phone",)
        indexes = [
            models.Index(fields=["user"]),
        ]
    
