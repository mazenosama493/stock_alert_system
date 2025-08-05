from django.core.management.base import BaseCommand
from stocks.models import Stock

STOCKS = [
    ('AAPL', 'Apple Inc.'),
    ('TSLA', 'Tesla Inc.'),
    ('GOOGL', 'Alphabet Inc.'),
    ('MSFT', 'Microsoft Corp'),
    ('AMZN', 'Amazon.com Inc.'),
    ('META', 'Meta Platforms Inc.'),
    ('NVDA', 'NVIDIA Corporation'),
    ('INTC', 'Intel Corporation'),
    ('NFLX', 'Netflix Inc.'),
    ('BABA', 'Alibaba Group'),
]

class Command(BaseCommand):
    help = 'Seed the database with predefined stocks'

    def handle(self, *args, **kwargs):
        for symbol, name in STOCKS:
            Stock.objects.get_or_create(symbol=symbol, company_name=name)
        self.stdout.write(self.style.SUCCESS('Seeded stock list.'))
