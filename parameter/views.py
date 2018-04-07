from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Parameter

class ParameterListView(ListView):
	model = Parameter

class ParameterDetailView(DetailView):
	model = Parameter