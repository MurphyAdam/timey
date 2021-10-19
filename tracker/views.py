from .serializers import TrackerSerializer, TrackerWriteSerializer
from timey.permissions import IsOwnerOrAdmin
from rest_framework import viewsets
from .models import Tracker


class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    permission_classes = [IsOwnerOrAdmin]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return TrackerWriteSerializer
        return TrackerSerializer
