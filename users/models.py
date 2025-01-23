from django.db import models
from django.contrib.auth.models import AbstractUser


from datetime import datetime
from dateutil.parser import parse as du_parse
from dateutil.relativedelta import relativedelta
from hashlib import sha1
from random import random

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from utils.sender import send_email


class User(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField( max_length=150, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=150, blank=True, verbose_name="Отчество")
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_executor = models.BooleanField(default=False, verbose_name='Исполнитель')
    is_dispatcher = models.BooleanField(default=False, verbose_name='Диспетчер')
    is_master = models.BooleanField(default=False, verbose_name='Мастер')
    is_duty_executor = models.BooleanField(default=False, verbose_name='Дежурный исполнитель')
    is_duty_dispatcher = models.BooleanField(default=False, verbose_name='Дежурный диспетчер')
    sections = models.ManyToManyField('MenuSections', verbose_name='Секции, разрешенные к показу', blank=True)
    job = models.CharField(max_length=150, verbose_name='Работа', blank=True)
    cookie_acceptance = models.BooleanField(default=False, verbose_name='Согласие использования файлов cookie')

    date_joined = last_login = None
    

    def __str__(self):
        return self.username
    
# class MenuSections(models.Model):
#     name = models.CharField(max_length=128,
#                             unique=True,
#                             verbose_name='Название')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Секция меню в шапке пользователя'
#         verbose_name_plural = 'Секции меню в шапке пользователя'


class Profile(models.Model):
    MALE = "M"
    FEMALE = "F"
    UNKNOWN = "U"

    GENDERS = (
        (MALE, "Мужской"),
        (FEMALE, "Женский"),
        (UNKNOWN, "Не указан"),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    gender = models.CharField(
        max_length=1, choices=GENDERS, default=UNKNOWN, verbose_name="Пол"
    )
    birthday_at = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    avatar = models.ImageField(
        upload_to="avatars", blank=True, null=True, verbose_name="Аватар"
    )
    activation_key = models.CharField(
        max_length=128, blank=True, verbose_name="Ключ активации"
    )
    activation_key_expires = models.DateTimeField(
        blank=True, null=True, verbose_name="Ключ активации годен до"
    )
    password_recovery_key = models.CharField(
        max_length=128, blank=True, verbose_name="Ключ восстановления пароля"
    )
    password_recovery_key_expires = models.DateTimeField(
        blank=True, null=True, verbose_name="Ключ восстановления пароля годен до"
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        # если вызов произошел из loaddata, то пропускаем
        if kwargs.get("raw", False):
            return

        migration_in_progress = sender._meta.object_name == "Migrate"
        if not migration_in_progress and created:
            Profile.objects.create(user=instance).save()

    def deactivate_user(self):
        self.user.is_active = False
        self.user.save()

    def activate_user(self):
        self.user.is_active = True
        self.user.save()

    def generate_activation_key(self):
        self.activation_key = sha1(str(random()).encode("utf8")).hexdigest()
        self.activation_key_expires = timezone.now() + timezone.timedelta(hours=48)
        self.save()

    def is_activation_key_expired(self):
        if timezone.now() < self.activation_key_expires:
            return False
        return True

    def send_verify_mail(self):
        pass
        # verify_link = reverse(
        #     "users:verify", args=[self.user.username, self.activation_key]
        # )
        # subject = "Активация аккаунта"
        # message = (
        #     f"Чтобы активировать аккаунт, перейдите по ссылке: "
        #     f"{settings.BASE_URL}{verify_link}"
        # )

        # return send_email(self.user.email, False) #subject, message

    def verify(self, username: str, activation_key: str) -> bool:
        if (
            self.user.username == username
            and self.activation_key == activation_key
            and not self.is_activation_key_expired()
        ):
            self.activate_user()
            self.activation_key = ""
            self.activation_key_expires = None
            self.save()
            self.save()
            return True
        return False

    def generate_password_recovery_key(self):
        self.password_recovery_key = sha1(str(random()).encode("utf8")).hexdigest()
        self.password_recovery_key_expires = timezone.now() + timezone.timedelta(
            hours=48
        )
        self.save()

    def is_password_recovery_key_expired(self):
        if timezone.now() < self.password_recovery_key_expires:
            return False
        return True

    def send_password_recovery_mail(self):
        recovery_link = reverse(
            "users:password-recovery-link",
            args=[self.user.email, self.password_recovery_key],
        )
        subject = "Восстановление пароля"
        message = (
            f"Ваш логин: {self.user.username} \n"
            f"Для восстановления пароля, перейдите по ссылке: "
            f"{settings.BASE_URL}{recovery_link}"
        )

        return send_email(self.user.email, subject, False, message)

    def recovery_valid(self, email: str, key: str):
        if (
            self.user.email == email
            and self.password_recovery_key == key
            and not self.is_password_recovery_key_expired()
        ):
            return True
        return False


    def get_user_age(self):

        try:
            birth = du_parse(str(self.birthday_at), dayfirst = True)
            today_date = du_parse(str(datetime.today()), dayfirst = True)
            delta = relativedelta(today_date, birth)

            return delta.years
        except:
            return 'дата рождения не указана'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


'''Модель для хранения избранных заявок'''
class Favourite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField("list_of_request.Articles", blank=True)


class MenuSections(models.Model):
    name = models.CharField(max_length=128,
                            unique=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция меню в шапке пользователя'
        verbose_name_plural = 'Секции меню в шапке пользователя'
