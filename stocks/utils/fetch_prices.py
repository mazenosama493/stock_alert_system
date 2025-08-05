import requests
from stocks.models import Stock, StockPrice
from django.utils import timezone
from django.conf import settings

API_KEY = settings.API_KEY

def fetch_stock_prices():
    for stock in Stock.objects.all():
        url = f"https://financialmodelingprep.com/api/v3/quote-short/{stock.symbol}?apikey={API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            if data and 'price' in data[0]:
                StockPrice.objects.create(
                    stock=stock,
                    price=data[0]['price'],
                    timestamp=timezone.now()
                )
                print(f"Fetched {stock.symbol}: {data[0]['price']}")
            else:
                print(f"No price found for {stock.symbol}")
        except Exception as e:
            print(f"Error fetching {stock.symbol}: {e}")
