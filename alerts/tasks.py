from celery import shared_task
from .utils.alert_utils import check_alerts

@shared_task
def check_alerts_task():
    check_alerts()