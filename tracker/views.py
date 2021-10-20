from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TrackerSerializer, TrackerWriteSerializer, PauseTrackerSerializer
from timey.permissions import IsOwnerOrAdmin
from .models import Tracker


class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return TrackerWriteSerializer
        return TrackerSerializer


class MyTrackerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        return user.tracker_entries.all()

    def get_serializer_class(self):
        return TrackerSerializer


class TrackerTimerStateViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return PauseTrackerSerializer
        return TrackerSerializer
