from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import RoutingAccept

class RoutingAcceptListView(ListView):
	model = RoutingAccept

class RoutingAcceptDetailView(DetailView):
	model = RoutingAccept