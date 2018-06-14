from django.shortcuts import render
from .models import Operation
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from serialnumber.models import SerialNumber

class OperationListView(ListView):
	model = Operation

class OperationDetailView(DetailView):
	model = Operation

def onwip(request,slug):
	query = SerialNumber.objects.filter(current_operation__slug = slug)
	print (query)
	return render(request, 'operation/operation_wip.html', {'object_list':query})