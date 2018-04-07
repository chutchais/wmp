from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Routing

class RoutingListView(ListView):
	model = Routing

class RoutingDetailView(DetailView):
	model = Routing