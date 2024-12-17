from django.db import models

# class SMS_Message(models.Model):
#     phone_number = models.CharField(max_length=15)
#     text_sms = models.TextField()
#     is_sent = models.BooleanField(default=False)
    
    
#     def __str__(self):
#         return f"SMS to {self.phone_number}:{self.text_sms}"
import pytz
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SmsTable(Base):
    __tablename__ = 'sms_table'

    id = Column(Integer, primary_key=True)
    application_id = Column(Integer, ForeignKey('application_form.id'))
    date_time = Column(DateTime)
    phone = Column(String)
    client_type = Column(String)
    sms_code = Column(String)
    status = Column(String)
    try_count = Column(Integer)
    send = Column(String)
    text_sms = Column(String)
    id_tele2 = Column(String)

    application = relationship("ArticlesForm", back_populates="sms_table")

    @property
    def attribute_labels(self):
        return {
            'application_id': 'id заявки',
            'date_time': 'Дата',
            'phone': 'Телефон',
            'client_type': 'Тип получателя',
            'sms_code': 'СМС код',
            'status': 'Статус',
            'try_count': 'Количество отправлений',
            'send': 'Идентификатор отправки',
            'text_sms': 'Текст СМС',
            'id_tele2': 'ID в системе Tele2'
        }

    def __init__(self, **kwargs):
        super(SmsTable, self).__init__(**kwargs)

    def rules(self):
        return []

# Set timezone

datetime.datetime.now(pytz.timezone('Asia/Krasnoyarsk'))

# Note: The ApplicationForm class is not provided in the original code, 
# so you'll need to define it separately if needed.


    
    
