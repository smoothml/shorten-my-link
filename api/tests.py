import os

from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import Urls
from .views import APP_BASE_URL


class UrlsTestCase(TestCase):
    """This class defines the test suite for the Urls model."""

    def setUp(self):
        self.long_url = 'http://batman.com'

    def test_model_can_create_shortened_url(self):
        """Test the Urls model can create a short url."""
        old_count = Urls.objects.count()

        url = Urls(url=self.long_url)
        url.save()

        new_count = Urls.objects.count()
        self.assertEqual(new_count - old_count, 1)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.url_data = {'url': 'http://batman.com'}
        self.response = self.client.post(
            reverse('create'),
            self.url_data,
            format="json")

    def test_api_can_create_a_short_url(self):
        """Test the api can create short url."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
