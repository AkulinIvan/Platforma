from django.db import models
from companies.models import Companies
from .models import User

class SpecialPermissions(models.Model):
    """
        Класс с описанием компетенцций и особых прав пользователей
    """
    title = 'Вид "Пользователя"'
    expert = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Эксперт',
        related_name='expert'
    )
    categories = models.ManyToManyField(
        Companies,
        related_name='category_list',
        verbose_name='Компании'
    )
    editor = models.BooleanField(
        verbose_name='Координатор',
        default=False
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            user = User.objects.get(id=self.expert.id)
            user.is_expert = True
            user.save()
        super(SpecialPermissions, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.expert}'

    class Meta:
        verbose_name = 'Особые права'
        verbose_name_plural = 'Особые права'
