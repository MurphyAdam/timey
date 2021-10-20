from django.urls import path
from .views import TrackerViewSet, MyTrackerViewSet, TrackerTimerStateViewSet
from rest_framework.urlpatterns import format_suffix_patterns

"""
    tracker_list and tracker_detail urls 
    and supported actions of TrackerViewSet
"""

tracker_list = TrackerViewSet.as_view({'get': 'list', 'post': 'create'})

tracker_detail = TrackerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

"""
    my_tracker_list and my_tracker_detail urls 
    and supported actions of MyTrackerViewSet
"""

my_tracker_list = MyTrackerViewSet.as_view({'get': 'list'})

my_tracker_detail = MyTrackerViewSet.as_view({
    'get': 'retrieve',
})

"""
    timer_state_tracker_list and timer_state_tracker_detail 
    urls and supported actions of MyTrackerViewSet
"""

timer_state_tracker_list = TrackerTimerStateViewSet.as_view({'get': 'list'})
timer_state_tracker_detail = TrackerTimerStateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
})

urlpatterns = [
    path('tracker', tracker_list, name='tracker-list'),
    path('tracker/<int:pk>', tracker_detail, name='tracker-detail'),
    path('tracker/my', my_tracker_list, name='my-tracker-list'),
    path('tracker/<int:pk>/my', my_tracker_detail, name='my-tracker-detail'),
    path('tracker/timer_state',
         timer_state_tracker_list, name='timer-state-tracker-list'),
    path('tracker/<int:pk>/timer_state',
         timer_state_tracker_detail, name='timer-state-tracker-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
