from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import ItemList

class ItemListListView(ListView):
	model = ItemList

class ItemListDetailView(DetailView):
	model = ItemList