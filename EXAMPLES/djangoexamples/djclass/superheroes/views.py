from django.views.generic import (
    TemplateView, ListView, CreateView, DetailView, UpdateView
)
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Superhero, City


class HomeView(TemplateView):
    template_name = 'superheroes/home.html'
    data = {
        'message': 'Welcome to the superheroes app for class-based views',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.data)
        return context

class HeroListView(ListView):
    model = Superhero

class HeroDetailView(DetailView):
    model = Superhero

class HeroListViewPlus(ListView):
    model = Superhero
    context_object_name = 'heroes'
    template_name = 'superheroes/superhero_list_plus.html'

class HeroDetailViewPlus(DetailView):
    model = Superhero
    context_object_name = 'hero'
    template_name = 'superheroes/superhero_detail_plus.html'

class HeroCreateView(CreateView):
    model = Superhero
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class CityCreateView(CreateView):
    model = City
    fields = ['name']
    success_url = reverse_lazy('superheroes:success')

class HeroUpdateView(UpdateView):
    model = Superhero
    # template = "hero_update.html"
    fields = ['name', 'real_name', 'secret_identity', 'city']
    success_url = reverse_lazy('superheroes:success')

class SuccessView(TemplateView):
    template_name = 'superheroes/success.html'
