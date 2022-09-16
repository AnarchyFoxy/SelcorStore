import os
from celery import Celery

# ustawienia modułu domyślnego dla celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refrstore.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
