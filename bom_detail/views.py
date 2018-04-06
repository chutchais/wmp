from django.shortcuts import render
from .models import Bom_Detail
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

class Bom_DetailListView(ListView):
	model = Bom_Detail

class Bom_DetailDetailView(DetailView):
	model = Bom_Detail