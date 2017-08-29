from django.db import models
import shortuuid

class Urls(models.Model):
    id = models.SlugField(default=shortuuid.ShortUUID().random(length=8),
                          primary_key=True)
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.url
