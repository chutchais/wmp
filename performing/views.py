from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Performing

class PerformingListView(ListView):
	model = Performing

class PerformingDetailView(DetailView):
	model = Performing