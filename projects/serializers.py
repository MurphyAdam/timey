from rest_framework import serializers
from accounts.models import User
from .models import Project


class ProjectReadSerializer(serializers.ModelSerializer):
    """
    This serializer is used for READ only operations on the Project model.
    """

    # We only return the list of user ids who have been assigned
    # this project, instead of serialized user objects
    assigned_to = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
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
    """
    This serializer is used for CREATE, UPDATE operations on the Project model.
    """

    # We receive list of user ids (ids[int] <= 0) by which we assign
    # users to a project
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'name', 'slug', 'description',
                  'status', 'created_date', 'updated_date',
                  'dead_line', 'days_to_deadline', 'reached_deadline',
                  'assigned_to')
