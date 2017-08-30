from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shorten_url/?$', views.create_short_url, name="create"),
    url(r'^(?P<short_id>[\w\d]+)/?$', views.redirect, name="redirect")
]
