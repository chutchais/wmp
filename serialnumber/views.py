from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import SerialNumber
from operation.models import Operation


class SerialNumberListView(ListView):
	model = SerialNumber

class SerialNumberDetailView(DetailView):
	model = SerialNumber