from rest_framework import serializers
from projects.serializers import ProjectReadSerializer
from accounts.serializers import UserSerializer
from projects.models import Project
from accounts.models import User
from .models import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    project = ProjectReadSerializer(read_only=True, many=False)
    url = serializers.HyperlinkedIdentityField(
        view_name="tracker-detail", read_only=True
    )

    class Meta:
        model = Tracker
        fields = ('id', 'user', 'project', 'url', 'start_time',
                  'end_time', 'seconds_paused', 'pause_time',
                  'status', 'hours', 'date_updated',
                  'total_hours', 'is_paused', 'is_closed')


class TrackerWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False)
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(), many=False)

    class Meta:
        model = Tracker
        fields = ('id', 'user', 'project', 'status', 'start_time',
                  'end_time', 'is_paused', 'is_closed', )

        read_only_fields = ('seconds_paused',
                            'pause_time', 'hours',
                            'date_updated', 'total_hours', )
