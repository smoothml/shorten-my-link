from django.db import models
import shortuuid
import os

APP_BASE_URL = 'https://shorten-my-link.herokuapp.com'


class Urls(models.Model):
    id = models.SlugField(default=shortuuid.ShortUUID().random(length=8),
                          primary_key=True)
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    def shortened_url(self):
        return os.path.join(APP_BASE_URL, self.id)
