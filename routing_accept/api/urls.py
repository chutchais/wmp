from django.conf.urls import url
from django.contrib import admin

from .views import (
    RoutingAcceptListAPIView,
    RoutingAcceptDetailAPIView,
    RoutingAcceptCreateAPIView,
    RoutingAcceptDeleteAPIView,
    RoutingAcceptUpdateAPIView
    )

urlpatterns = [
	url(r'^$', RoutingAcceptListAPIView.as_view(), name='list'),
	url(r'^create/$',RoutingAcceptCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',RoutingAcceptDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', RoutingAcceptDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', RoutingAcceptUpdateAPIView.as_view(),name='update'),
 
]