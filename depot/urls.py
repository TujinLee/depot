from django.conf.urls.defaults import patterns, include, url
from .view import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)
