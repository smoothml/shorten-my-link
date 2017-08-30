from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^shorten_url$', views.create_short_url, name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
