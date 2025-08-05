from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ['user']
    def validate(self, data):
        alert_type = data.get('alert_type')
        duration = data.get('duration_minutes')

        if alert_type == 'threshold' and duration is not None:
            raise serializers.ValidationError({
                'duration_minutes': 'Must be null when alert_type is "threshold".'
            })
        elif alert_type == 'duration' and duration is None:
            raise serializers.ValidationError({
                'duration_minutes': 'Must not be null when alert_type is "duration".'
            })

        return data