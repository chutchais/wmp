from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Product

class ProductListView(ListView):
	model = Product

class ProductDetailView(DetailView):
	model = Product