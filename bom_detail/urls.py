from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (Bom_DetailDetailView,
					Bom_DetailListView)


urlpatterns = [
	# Page
	url(r'^$',Bom_DetailListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',Bom_DetailDetailView.as_view(),name='detail'),
]