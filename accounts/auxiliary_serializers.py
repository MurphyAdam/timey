from rest_framework import serializers
from .models import User


class BasicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_superuser',
                  'user_permissions', 'links', 'user_type')
