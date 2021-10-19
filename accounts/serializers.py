from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User
from .constants import API_USER_TYPE


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_superuser',
                  'user_permissions', 'links', 'user_type',
                  'email_verified',)


class CustomRegisterSerializer(RegisterSerializer):
    user_type = serializers.ChoiceField(
        choices=API_USER_TYPE, required=True, write_only=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'user_type': self.validated_data.get('user_type', ''),
        }


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')
