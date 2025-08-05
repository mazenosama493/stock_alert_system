from django.core.exceptions import ValidationError
from stocks.management.commands.seed_stocks import STOCKS


ALLOWED_SYMBOLS = [symbol for symbol, _ in STOCKS]

def validate_stock_symbol(value):
        if value not in ALLOWED_SYMBOLS:
            raise ValidationError(f"{value} is not a valid stock symbol.")