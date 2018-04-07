from django.conf.urls import url
from django.contrib import admin

from .views import (
    RoutingNextListAPIView,
    RoutingNextDetailAPIView,
    RoutingNextCreateAPIView,
    RoutingNextDeleteAPIView,
    RoutingNextUpdateAPIView
    )

urlpatterns = [
	url(r'^$', RoutingNextListAPIView.as_view(), name='list'),
	url(r'^create/$',RoutingNextCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',RoutingNextDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', RoutingNextDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', RoutingNextUpdateAPIView.as_view(),name='update'),
 
]