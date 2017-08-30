from rest_framework import serializers
from .models import Urls


class UrlsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Urls
        fields = ('id', 'url', 'pub_date')
        read_only_fields = ('id', 'pub_date')
