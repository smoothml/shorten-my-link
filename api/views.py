import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UrlsSerializer

APP_BASE_URL = 'https://shorten-my-link.herokuapp.com'


@api_view(['POST'])
def create_short_url(request):
    serializer = UrlsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'shortened_url': os.path.join(APP_BASE_URL, serializer.data['id'])},
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
