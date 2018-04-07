from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import RoutingReject

class RoutingRejectListView(ListView):
	model = RoutingReject

class RoutingRejectDetailView(DetailView):
	model = RoutingReject