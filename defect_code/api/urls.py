from django.conf.urls import url
from django.contrib import admin

from .views import (
    DefectCodeListAPIView,
    DefectCodeDetailAPIView,
    DefectCodeCreateAPIView,
    DefectCodeDeleteAPIView,
    DefectCodeUpdateAPIView
    )

urlpatterns = [
	url(r'^$', DefectCodeListAPIView.as_view(), name='list'),
	url(r'^create/$', DefectCodeCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$', DefectCodeDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', DefectCodeDeleteAPIView.as_view(),name='delete'),
	url(r'^(?P<slug>[\w-]+)/update/$', DefectCodeUpdateAPIView.as_view(),name='update'),
 
]