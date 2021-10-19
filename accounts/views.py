from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` 
    actions for the Users viewset. It is only available to 
    authenticated admin users.
    """
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication
    ]

    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
