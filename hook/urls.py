from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import (HookDetailView,
					HookListView)


urlpatterns = [
	# Page
	url(r'^$',HookListView.as_view(),name='list'),
    url(r'^(?P<slug>[-\w]+)/$',HookDetailView.as_view(),name='detail'),
]