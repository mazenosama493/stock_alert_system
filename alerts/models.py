# alerts/models.py

from django.db import models
from django.contrib.auth.models import User
from .validators import validate_stock_symbol
from django.core.exceptions import ValidationError
from django.utils import timezone

class Alert(models.Model):
    ALERT_TYPE_CHOICES = [
        ('threshold', 'Threshold'),
        ('duration', 'Duration'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10,validators=[validate_stock_symbol])
    alert_type = models.CharField(max_length=10, choices=ALERT_TYPE_CHOICES)
    threshold_price = models.FloatField(null=True, blank=True)
    comparison = models.CharField(max_length=5, choices=[('gt', '>'), ('lt', '<')])
    duration_minutes = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol} {self.comparison} {self.threshold_price}"

