from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import WorkOrder

class WorkOrderListView(ListView):
	model = WorkOrder

class WorkOrderDetailView(DetailView):
	model = WorkOrder