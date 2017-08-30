import os

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UrlsSerializer
from .models import Urls

APP_BASE_URL = 'https://shorten-my-link.herokuapp.com'


@api_view(['POST'])
def create_short_url(request):
    serializer = UrlsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'shortened_url': os.path.join(APP_BASE_URL, serializer.data['id'])},
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def redirect(request, short_id):
    url = get_object_or_404(Urls, pk=short_id)
    return HttpResponseRedirect(url.url)
