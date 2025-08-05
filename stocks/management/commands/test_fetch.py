from django.core.management.base import BaseCommand
from stocks.utils.fetch_prices import fetch_stock_prices

class Command(BaseCommand):
    help = 'Fetch latest stock prices for all predefined stocks'

    def handle(self, *args, **kwargs):
        fetch_stock_prices()
