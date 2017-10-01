from django.conf.urls import url
from django.contrib import admin

from .views import (
    ItemListListAPIView,
    ItemListDetailAPIView,
    ItemListCreateAPIView,
    ItemListDeleteAPIView,
    ItemListUpdateAPIView
    )

urlpatterns = [
	url(r'^$', ItemListListAPIView.as_view(), name='list'),
	url(r'^create/$',ItemListCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',ItemListDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', ItemListDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', ItemListUpdateAPIView.as_view(),name='update'),
 
]