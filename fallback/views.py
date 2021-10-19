from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class FallbackView(GenericAPIView):
    """
    Catches '' and non-existent urls
    """

    def get(self, request, path=None):

        data = {
            'message': 'You have reached Timey server. To view available API points, '
            'please head to http://127.0.0.1:8000/api/',
        }
        return Response(data, status=200)
