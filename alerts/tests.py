from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Alert
from stocks.management.commands.seed_stocks import STOCKS

class AlertTests(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='testpassword123'
        )
        
        # Get a valid stock symbol
        self.valid_symbol = STOCKS[0][0] if STOCKS else 'AAPL'
        
        # Create test alerts
        self.threshold_alert = Alert.objects.create(
            user=self.user,
            stock_symbol=self.valid_symbol,
            alert_type='threshold',
            threshold_price=100.0,
            comparison='gt',
            is_active=True
        )
        
        self.duration_alert = Alert.objects.create(
            user=self.user,
            stock_symbol=self.valid_symbol,
            alert_type='duration',
            duration_minutes=30,
            is_active=True
        )
        
        # URLs
        self.alert_list_url = reverse('alert-list')
        self.alert_detail_url = reverse('alert-detail', kwargs={'pk': self.threshold_alert.pk})
        
        # Authenticate
        self.client.force_authenticate(user=self.user)


    # Threshold alert tests
    def test_create_valid_threshold_alert(self):
        data = {
            'stock_symbol': self.valid_symbol,
            'alert_type': 'threshold',
            'threshold_price': 150.0,
            'comparison': 'lt',
            'is_active': True,
            'duration_minutes': None  # Explicitly null
        }
        response = self.client.post(self.alert_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Alert.objects.count(), 3)

    def test_threshold_alert_with_duration_fails(self):
        data = {
            'stock_symbol': self.valid_symbol,
            'alert_type': 'threshold',
            'threshold_price': 150.0,
            'comparison': 'lt',
            'is_active': True,
            'duration_minutes': 30  # Invalid for threshold
        }
        response = self.client.post(self.alert_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('duration_minutes', response.data)


    def test_duration_alert_missing_duration_fails(self):
        data = {
            'stock_symbol': self.valid_symbol,
            'alert_type': 'duration',
            'comparison': 'lt',
            'is_active': True
        }
        response = self.client.post(self.alert_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('duration_minutes', response.data)

    def test_duration_alert_with_invalid_duration_fails(self):
        for invalid_duration in [0, -10]:
            data = {
                'stock_symbol': self.valid_symbol,
                'alert_type': 'duration',
                'duration_minutes': invalid_duration,
                'comparison': 'lt',
                'is_active': True
            }
            response = self.client.post(self.alert_list_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('duration_minutes', response.data)

    # Default is_active tests
    def test_is_active_defaults_to_true(self):
        data = {
            'stock_symbol': self.valid_symbol,
            'alert_type': 'threshold',
            'threshold_price': 100.0,
            'comparison': 'gt'
            # Omitted is_active
        }
        response = self.client.post(self.alert_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['is_active'])

    # Read-only user field test
    def test_user_field_is_read_only(self):
        data = {
            'stock_symbol': self.valid_symbol,
            'alert_type': 'threshold',
            'threshold_price': 100.0,
            'comparison': 'gt',
            'is_active': True,
            'user': self.other_user.id  # Should be ignored
        }
        response = self.client.post(self.alert_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.id)  # Still set to authenticated user