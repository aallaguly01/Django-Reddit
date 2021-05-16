import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reddit.settings')

app = Celery('reddit')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'src.blog.tasks.send_view_count_report',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}
# celery -A reddit worker -l info
# celery -A reddit beat
