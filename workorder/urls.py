from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (WorkOrderDetailView,
					WorkOrderListView)


urlpatterns = [
	# Page
	url(r'^$',WorkOrderListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',WorkOrderDetailView.as_view(),name='detail'),
]