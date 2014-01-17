#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('cms',
    url(r'^$', 'views.home'),
)
