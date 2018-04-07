from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import RoutingNext

class RoutingNextListView(ListView):
	model = RoutingNext

class RoutingNextDetailView(DetailView):
	model = RoutingNext