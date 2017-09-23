from django.conf.urls import url
from django.contrib import admin

from .views import (
    RoutingDetailListAPIView,
    RoutingDetailDetailAPIView,
    RoutingDetailCreateAPIView,
    RoutingDetailDeleteAPIView,
    RoutingDetailUpdateAPIView
    )

urlpatterns = [
	url(r'^$', RoutingDetailListAPIView.as_view(), name='list'),
	url(r'^create/$',RoutingDetailCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',RoutingDetailDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\wRouting-]+)/delete/$', RoutingDetailDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', RoutingDetailUpdateAPIView.as_view(),name='update'),
 
]