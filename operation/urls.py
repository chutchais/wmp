from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (OperationDetailView,
					OperationListView)


urlpatterns = [
	# Page
	url(r'^$',OperationListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',OperationDetailView.as_view(),name='detail'),
]