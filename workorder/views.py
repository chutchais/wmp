from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import WorkOrder
from serialnumber.models import SerialNumber

class WorkOrderListView(ListView):
	model = WorkOrder

class WorkOrderDetailView(DetailView):
	model = WorkOrder


def onwip(request,slug):
	query = SerialNumber.objects.filter(current_operation__slug = slug)
	return render(request, 'workorder/workorder_wip.html', {'object_list':query})