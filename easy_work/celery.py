import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easy_work.settings')

app = Celery('easy_work')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parser': {
        'task': 'celery_app.tasks.parser',
        'schedule': crontab(minute="*/1"),
        #'schedule': crontab(hour=7, minute=30, day_of_week=1),
    },

    # 'test_beat': {
    #         'task': 'celery_app.tasks.send_mail_reminder',
    #         #'schedule': crontab(minute='*/5'),
    #         'schedule': timedelta(seconds=30),
    #     },
}