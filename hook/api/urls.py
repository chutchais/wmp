from django.conf.urls import url
from django.contrib import admin

from .views import (
    HookListAPIView,
    HookDetailAPIView,
    HookCreateAPIView,
    HookDeleteAPIView,
    HookUpdateAPIView
    )

urlpatterns = [
	url(r'^$', HookListAPIView.as_view(), name='list'),
	url(r'^create/$',HookCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',HookDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', HookDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', HookUpdateAPIView.as_view(),name='update'),
 
]