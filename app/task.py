
from django.core.mail import send_mail
from django.conf import settings
from .models import Stock


def send_stock_alert(stock):
    """
    Sends an email alert for a stock whose percentage change exceeds the threshold.
    """
    subject = f'Stock Alert: {stock.symbol}'
    message = (
        f'Stock: {stock.name} ({stock.symbol})\n'
        f'Price: ${stock.price}\n'
        f'Percentage Change: {stock.percent}%\n'
        f'Last Updated: {stock.last_updated}\n'
    )
    recipient_list = ['recipient@example.com']  # Replace with actual recipient emails

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,  # Raise an exception if email fails
        )
        print(f"Email sent for {stock.symbol}")  # Log success
    except Exception as e:
        print(f"Failed to send email for {stock.symbol}: {e}")  # Log failure



from django.core.mail import send_mail
from django.conf import settings
from .models import Stock


def send_stock_alert(stock):
    """
    Sends an email alert for a stock whose percentage change exceeds the threshold.
    """
    subject = f'Stock Alert: {stock.symbol}'
    message = (
        f'Stock: {stock.name} ({stock.symbol})\n'
        f'Price: ${stock.price}\n'
        f'Percentage Change: {stock.percent}%\n'
        f'Last Updated: {stock.last_updated}\n'
    )
    recipient_list = ['recipient@example.com']  # Replace with actual recipient emails

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,  # Raise an exception if email fails
        )
        print(f"Email sent for {stock.symbol}")  # Log success
    except Exception as e:
        print(f"Failed to send email for {stock.symbol}: {e}")  # Log failure


def check_stock_alerts():
    stocks = Stock.objects.all()
    for stock in stocks:
       
        if stock.percent is not None and abs(stock.percent) > 5:
            send_stock_alert(stock)  