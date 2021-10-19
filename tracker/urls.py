from django.urls import path
from .views import TrackerViewSet
from rest_framework.urlpatterns import format_suffix_patterns

tracker_list = TrackerViewSet.as_view({'get': 'list', 'post': 'create'})

tracker_detail = TrackerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('tracker', tracker_list, name='tracker-list'),
    path('tracker/<int:pk>', tracker_detail, name='tracker-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
