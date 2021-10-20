from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from timey.permissions import IsOwnerOrAdminOrReadOnly
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` 
    actions for the Users viewset. It is only available to 
    authenticated admin users.
    """

    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
