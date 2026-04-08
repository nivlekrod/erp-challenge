from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_challenge.settings')

app = Celery('principal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

app.autodiscover_tasks()

app.conf.timezone = 'America/Belem'

TASKS = {
    'create_customer_file': {
        'task': 'principal.tasks.create_customer_file',
        'schedule': 5
    }
}

app.conf.beat_schedule = TASKS