import os
from celery import Celery
from .settings import INSTALLED_APPS


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
app = Celery('library', backend='amqp', broker='amqp://')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))