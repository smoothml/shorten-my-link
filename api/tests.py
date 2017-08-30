import os

from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

from .models import Urls


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
            format="json"
        )

    def test_api_can_create_a_short_url(self):
        """Test the api can create short url."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_redirect_to_long_url(self):
        """Test the api can redirect to the original long url."""
        long_url = self.response.data['shortened_url']
        short_id = long_url.split('/')[-1]
        response = self.client.get(
            reverse('redirect', kwargs={'short_id': short_id}),
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
