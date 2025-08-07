from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ['user']
    def validate(self, data):
        alert_type = data.get('alert_type')
        duration_minutes = data.get('duration_minutes')
        threshold_price = data.get('threshold_price')

        if threshold_price<0:
            raise serializers.ValidationError({
                'threshold_price': 'Threshold price must be positive number.'
            })


        if alert_type == 'threshold':
            if duration_minutes is not None:
                raise serializers.ValidationError({
                    'duration_minutes': 'Must be null for threshold alerts.'
                })

        elif alert_type == 'duration':
            if duration_minutes is None:
                raise serializers.ValidationError({
                    'duration_minutes': 'This field is required for duration alerts.'
                })
            elif duration_minutes <=0:
                raise serializers.ValidationError({
                    'duration_minutes': 'Duration must be greater than 0 for duration alerts.'
                })

        return data