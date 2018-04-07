from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Snippet

class SnippetListView(ListView):
	model = Snippet

class SnippetDetailView(DetailView):
	model = Snippet