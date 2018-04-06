from django.shortcuts import render
from .models import Operation
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

class OperationListView(ListView):
	model = Operation

class OperationDetailView(DetailView):
	model = Operation