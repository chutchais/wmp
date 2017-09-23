from django.conf.urls import url
from django.contrib import admin

from .views import (
    BomDetailListAPIView,
    BomDetailDetailAPIView,
    BomDetailCreateAPIView,
    BomDetailDeleteAPIView,
    BomDetailUpdateAPIView
    )

urlpatterns = [
	url(r'^$', BomDetailListAPIView.as_view(), name='list'),
	url(r'^create/$',BomDetailCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$',BomDetailDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', BomDetailDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', BomDetailUpdateAPIView.as_view(),name='update'),
 
]