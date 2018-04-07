from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Item

class ItemListView(ListView):
	model = Item

class ItemDetailView(DetailView):
	model = Item


