from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



from handbook.models import Roles

# class User(AbstractUser):
#     first_name = models.CharField(max_length=150, verbose_name='Имя')
#     last_name = models.CharField( max_length=150, verbose_name='Фамилия')
#     patronymic = models.CharField(max_length=150, blank=True, verbose_name="Отчество")
#     is_admin = models.BooleanField(default=False, verbose_name='Администратор')
#     is_executor = models.BooleanField(default=False, verbose_name='Исполнитель')
#     is_dispatcher = models.BooleanField(default=False, verbose_name='Диспетчер')
#     is_master = models.BooleanField(default=False, verbose_name='Мастер')
#     is_duty_executor = models.BooleanField(default=False, verbose_name='Дежурный исполнитель')
#     is_duty_dispatcher = models.BooleanField(default=False, verbose_name='Дежурный диспетчер')
    
    

#     def __str__(self):
#         return self.username
    
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, null=True, blank=True, verbose_name="Роль", default=None, on_delete=models.PROTECT)
    phone = PhoneNumberField('Номер телефона', max_length=50, default='Не указан номер')
    nomer_ATS = models.IntegerField('Номер АТС', null=True)
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_coordinator = models.BooleanField(default=False, verbose_name='Координатор')
    is_executor = models.BooleanField(default=False, verbose_name='Исполнитель')
    is_dispatcher = models.BooleanField(default=False, verbose_name='Диспетчер')
    is_master = models.BooleanField(default=False, verbose_name='Мастер')
    is_duty_executor = models.BooleanField(default=False, verbose_name='Дежурный исполнитель')
    is_duty_dispatcher = models.BooleanField(default=False, verbose_name='Дежурный диспетчер')
    
    class Meta:
        db_table = 'userprofile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ("phone",)
        indexes = [
            models.Index(fields=["user"]),
        ]
    



# class SpecialPermissions(models.Model):
#     """
#         Класс с описанием компетенцций и особых прав пользователей
#     """
#     title = 'Вид "Пользователя"'
#     admin = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         verbose_name='Эксперт',
#         related_name='expert'
#     )
#     company = models.ManyToManyField(
#         Companies,
#         related_name='category_list',
#         verbose_name='Компетенции эксперта'
#     )
#     dispatcher = models.BooleanField(
#         verbose_name='Диспетчер',
#         default=False
#     )
#     admin_competencies = models.ManyToManyField(
#         verbose_name='Компетенции руководителя',
#         to=Companies,
#         related_name='special_permissions'
#     )

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             user = User.objects.get(id=self.expert.id)
#             user.is_expert = True
#             user.save()
#         super(SpecialPermissions, self).save(*args, **kwargs)

#     def __str__(self):
#         return f'{self.admin}'

#     class Meta:
#         verbose_name = 'Особые права'
#         verbose_name_plural = 'Особые права'