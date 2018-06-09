from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from hook.models import Hook

class HookListView(ListView):
	model = Hook

class HookDetailView(DetailView):
	model = Hook