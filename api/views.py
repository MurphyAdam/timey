from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    This is the api root view. It provides the available views.
    """
    return Response({
                    'Users': reverse('user-list', request=request, format=format),
                    'Projects': reverse('projects-list', request=request, format=format),
                    'Tracker': reverse('tracker-list', request=request, format=format),
                    'My Tracker Entries': reverse('my-tracker-list', request=request, format=format),
                    'Tracker timer-state': reverse('timer-state-tracker-list',
                                                   request=request, format=format),
                    })
