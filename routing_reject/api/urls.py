from django.conf.urls import url
from django.contrib import admin

from .views import (
    RoutingRejectListAPIView,
    RoutingRejectDetailAPIView,
    RoutingRejectCreateAPIView,
    RoutingRejectDeleteAPIView,
    RoutingRejectUpdateAPIView
    )

urlpatterns = [
	url(r'^$', RoutingRejectListAPIView.as_view(), name='list'),
	url(r'^create/$',RoutingRejectCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',RoutingRejectDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', RoutingRejectDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', RoutingRejectUpdateAPIView.as_view(),name='update'),
 
]