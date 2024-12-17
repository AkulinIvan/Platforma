
app.conf.beat_schedule = {
    'send-sms-daily': {
        'task': 'your_app.tasks.schedule_send_sms',
        'schedule': crontab(minute=0, hour=0),  # Выполнять ежедневно в полночь
    },
}


# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery


# os.environ.setdefault('DJA  NGO_SETTINGS_MODULE', 'ADS.settings')

# app = Celery('ADS')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()