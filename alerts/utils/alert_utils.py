
from alerts.models import Alert
from stocks.models import StockPrice, Stock  # assuming this stores latest prices
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings

def check_alerts():
    alerts = Alert.objects.filter(is_active=True)

    for alert in alerts:
        try:
            stock = Stock.objects.get(symbol=alert.stock_symbol)
        except Stock.DoesNotExist:
            continue

        prices = StockPrice.objects.filter(stock=stock, timestamp__gte=alert.created_at).order_by('-timestamp')
        if not prices:
            alert.is_active = False
            alert.save()
            continue

        price= prices[0].price


        # Instant threshold check
        if alert.alert_type == 'threshold':
            if (alert.comparison == 'gt' and price > alert.threshold_price) or \
               (alert.comparison == 'lt' and price < alert.threshold_price):
                trigger_alert(alert, price)

        # Duration check using created_at as fixed reference
        elif alert.alert_type == 'duration':
            now = timezone.now()
            timer=alert.created_at
            duration = timedelta(minutes=alert.duration_minutes)

            # Fetch all recent prices within the duration window
            prices = StockPrice.objects.filter(
                stock=stock,
                timestamp__gte=alert.created_at
            ).order_by('timestamp')

            if not prices.exists():
                continue

            # Check if all prices in the window meet the condition
            if alert.comparison == 'gt':
                all_satisfied = all(p.price > alert.threshold_price for p in prices)
            else:  # 'lt'
                all_satisfied = all(p.price < alert.threshold_price for p in prices)

            # Check if the full duration has passed since the last reset
            end_time =timer+duration

            if all_satisfied and now >= end_time:
                trigger_alert(alert, prices.last().price)

            elif not all_satisfied:
                # Reset the timer
                timer = now




def trigger_alert(alert, current_price):
    alert.is_active = False
    alert.save()

    if alert.alert_type == 'duration':
        message=f"Your alert for {alert.stock_symbol} has been triggered. Current price: {current_price}. the price has been more than {alert.threshold_price} for {alert.duration_minutes} minutes."
    else:
        message=f"Your alert for {alert.stock_symbol} has been triggered. Current price: {current_price}"

    # Log or send email
    send_mail(
        subject="Stock Alert Triggered",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[alert.user.email],
        fail_silently=True,
    )

    print(f"Alert triggered for {alert.stock_symbol} at price {current_price}")
