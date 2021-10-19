from django.urls import path
from .views import ProjectViewSet
from rest_framework.urlpatterns import format_suffix_patterns

project_list = ProjectViewSet.as_view({'get': 'list', 'post': 'create'})

project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('projects', project_list, name='projects-list'),
    path('projects/<int:pk>', project_detail, name='project-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
