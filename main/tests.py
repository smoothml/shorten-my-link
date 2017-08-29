from django.test import TestCase
from .models import Urls


class UrlsTestCase(TestCase):

    def test_model_can_create_shortened_url(self):
        old_count = Urls.objects.count()

        long_url = 'www.batman.com'
        url = Urls(url=long_url)
        url.save()

        new_count = Urls.objects.count()
        self.assertEqual(new_count - old_count, 1)
