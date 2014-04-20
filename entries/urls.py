# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from entries import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^entry/(?P<entry_id>\d+)/$', views.entry_page, name='entry_page'),
    url(r'^by_tag/(?P<tag_id>\d+)/$', views.posts_by_tag, name='posts_by_tag'),
)

