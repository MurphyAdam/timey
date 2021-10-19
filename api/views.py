from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    This is the api root view. It provides the available views.
    """
    return Response({
                    'users': reverse('user-list', request=request, format=format),
                    'projects': reverse('projects-list', request=request, format=format),
                    'tracker': reverse('tracker-list', request=request, format=format),
                    })
