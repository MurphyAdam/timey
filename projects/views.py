from .serializers import ProjectReadSerializer, ProjectWriteSerializer
from timey.permissions import IsOwnerOrAdminOrReadOnly
from rest_framework import viewsets
from .models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return ProjectWriteSerializer
        return ProjectReadSerializer
