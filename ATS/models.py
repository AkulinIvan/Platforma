from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    name = models.OneToOneField(User, related_name='Пользователь', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, unique=True)
    
    def __str__(self):
        return f"{self.phone_number}"
    
    
class CallLog(models.Model):
    caller = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, related_name='caller')
    callee = models.CharField(max_length=50)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    recording = models.FileField(upload_to='recordings/')

    def __str__(self):
        return f"{self.callee} - {self.caller.name} at {self.start_time}"
    
    class Meta:
        db_table = 'call_log'
        verbose_name = 'Запись звонка'
        verbose_name_plural = 'Записи звонков'
        ordering = ("id",)
        indexes = [
            models.Index(fields=["caller"]),
        ]
        
    def duration(self):
        if self.end_time is not None:
            return self.end_time - self.start_time
        else:
            return datetime.now() - self.start_time
