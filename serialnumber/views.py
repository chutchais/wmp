from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import SerialNumber

class SerialNumberListView(ListView):
	model = SerialNumber

class SerialNumberDetailView(DetailView):
	model = SerialNumber