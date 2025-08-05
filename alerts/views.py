from rest_framework import viewsets, permissions
from .models import Alert
from .serializers import AlertSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.utils import timezone

class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance=serializer.save(user=self.request.user)
        instance.created_at = timezone.now()
        instance.save()

    @action(detail=False, methods=['delete'], permission_classes=[permissions.IsAuthenticated])
    def delete_all(self, request):
        user_alerts = Alert.objects.filter(user=self.request.user)
        count, _ = user_alerts.delete()
        return Response({'deleted_alerts': count}, status=status.HTTP_200_OK)