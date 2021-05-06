from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from .forms import CarFormSet
from .models import Car

def home(request):
    return HttpResponse("Welcome to Car Lot")

class CarListView(ListView):
    model = Car

class CarAddView(TemplateView):
    template_name = 'car_lot/car_add.html'

    def get(self, *args, **kwargs):
        formset = CarFormSet(queryset=Car.objects.all())  # start empty
        return self.render_to_response({'car_formset': formset})

    def post(self, *args, **kwargs):
        formset = CarFormSet(data=self.request.POST)

        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("car_lot:list"))

        return self.render_to_response({'car_formset': formset})



