from rest_framework import serializers
from projects.serializers import ProjectReadSerializer
from accounts.serializers import UserSerializer
from projects.models import Project
from accounts.models import User
from .models import Tracker
from .constants import TIMER_ACTION


class TrackerSerializer(serializers.ModelSerializer):
    """
    This serializer is used for READ only operations on the Tracker model.
    """

    user = UserSerializer(read_only=True, many=False)
    project = ProjectReadSerializer(read_only=True, many=False)
    entry_detail_url = serializers.HyperlinkedIdentityField(
        view_name="tracker-detail", read_only=True
    )
    entry_timer_state_url = serializers.HyperlinkedIdentityField(
        view_name="timer-state-tracker-detail", read_only=True
    )

    class Meta:
        model = Tracker
        fields = ('id', 'user', 'project', 'entry_detail_url', 'entry_timer_state_url',
                  'state', 'start_time',
                  'end_time', 'seconds_paused', 'pause_time',
                  'status', 'hours', 'date_updated',
                  'total_hours', 'is_paused', 'is_closed')


class TrackerWriteSerializer(serializers.ModelSerializer):
    """
    This serializer is used for CREATE, UPDATE only operations on the Tracker model.
    """

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

    def to_representation(self, instance):
        """
        We use to_representation because we want to recieve data in one format, 
        but return it in another.
        This class (TrackerWriteSerializer) is mainly for creating/updating Tracker entries, 
        but it is also used by default to return the created/ updated record(s), 
        which is indesirable since for example we will be getting a project id, 
        and a user id as a JSON response instead of a serialized user/ project object.
        """
        # context will be needed TrackerSerializer url field which is using
        # the HyperlinkedIdentityField
        request = self.context['request']
        serializer = TrackerSerializer(instance, context={'request': request})
        return serializer.data


class PauseTrackerSerializer(TrackerWriteSerializer):
    """
    This serializer is used for READ only operations on the Tracker model.
    """

    class Meta:
        model = Tracker
        fields = ('timer_state', )

    def update(self, instance, validated_data):
        timer_state = validated_data.get("timer_state", None)
        if timer_state == TIMER_ACTION.PAUSE:
            instance.pause()
        elif timer_state == TIMER_ACTION.UNPAUSE:
            instance.unpause()
        elif timer_state == TIMER_ACTION.TOGGLE:
            instance.toggle_paused()
        instance.save()
        return instance
