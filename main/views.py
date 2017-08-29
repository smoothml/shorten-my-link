from rest_framework import generics
from .serializers import UrlsSerializer
from .models import Urls


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
