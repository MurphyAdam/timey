from rest_framework import serializers
from accounts.serializers import UserSerializer
from accounts.models import User
from .models import Project


class ProjectReadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(many=True, read_only=False)
    url = serializers.HyperlinkedIdentityField(
        view_name="project-detail", read_only=True
    )

    class Meta:
        model = Project
        fields = ('id', 'name', 'slug', 'url', 'description',
                  'status', 'created_date', 'updated_date',
                  'dead_line', 'days_to_deadline', 'reached_deadline',
                  'assigned_to')


class ProjectWriteSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'slug', 'description',
                  'status', 'created_date', 'updated_date',
                  'dead_line', 'days_to_deadline', 'reached_deadline',
                  'assigned_to')
