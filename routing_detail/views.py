from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from routing_detail.models import RoutingDetail

class RoutingDetailListView(ListView):
	model = RoutingDetail

class RoutingDetailDetailView(DetailView):
	model = RoutingDetail