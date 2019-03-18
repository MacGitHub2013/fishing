from django.shortcuts import render
from . models import Fish
from django.urls import reverse_lazy
from django.views.generic import (
ListView, 
DetailView,
CreateView,
DeleteView,
UpdateView
) 
# Create your views here.


class FishListView(ListView):
    queryset = Fish.objects.all()

class FishSearchView(ListView):
    
    def get_queryset(self):
        key = self.kwargs.get("key")
        if key :
            queryset = Fish.objects.filter(fish_type=key)
        else:
            queryset = Fish.objects.all()

        return queryset

class FishDetailsView(DetailView):
    queryset = Fish.objects.all()
    context_object_name='Fish'

class FishCreateView(CreateView):
    model =Fish
    fields =('name','fish_type','alias')

class FishUpdateView(UpdateView):
    model =Fish
    fields =('name','fish_type','alias')
    success_url = './'

class FishDeleteView(DeleteView):
    model = Fish
    success_url = reverse_lazy('fish-list')