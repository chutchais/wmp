from django.conf.urls import url
from django.contrib import admin

from .views import (
    SnippetListAPIView,
    SnippetDetailAPIView,
    SnippetCreateAPIView,
    SnippetDeleteAPIView,
    SnippetUpdateAPIView
    )

urlpatterns = [
	url(r'^$', SnippetListAPIView.as_view(), name='list'),
	url(r'^create/$',SnippetCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',SnippetDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', SnippetDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', SnippetUpdateAPIView.as_view(),name='update'),
 
]