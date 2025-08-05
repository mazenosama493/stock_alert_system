from celery import shared_task
from .utils.fetch_prices import fetch_stock_prices

@shared_task
def fetch_stock_prices_task():
    fetch_stock_prices()
