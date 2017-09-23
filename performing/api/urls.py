from django.conf.urls import url
from django.contrib import admin

from .views import (
    PerformingListAPIView,
    PerformingDetailAPIView,
    PerformingCreateAPIView,
    PerformingDeleteAPIView,
    PerformingUpdateAPIView
    )

urlpatterns = [
	url(r'^$', PerformingListAPIView.as_view(), name='list'),
	url(r'^create/$', PerformingCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PerformingDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', PerformingDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', PerformingUpdateAPIView.as_view(),name='update'),
 
]