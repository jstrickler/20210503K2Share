"""
    Views for the DJForms Project

    These are forms illustrating how forms work in Django
"""
from django.shortcuts import get_object_or_404, render
from .forms import HeroFormSet
from .models import Superhero

def home(request):
    """
    Welcome page

    :param request: HTTP request
    :return: HTTP Response
    """
    data = {
        'message': 'Welcome to the superheroes app for forms',
    }
    return render(request, 'home.html', data)


def heroformset(request):
    """

    :param request: HTTP request
    :return: HTTP Response
    """

    # get initial data here if needed

    # bound (filled-in) form
    if request.method == 'POST':
        formset = HeroFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
            hero_name = form.cleaned_data['hero_name']
            hero_color = form.cleaned_data['hero_color']
            request.session['color'] = hero_color
            hero = get_object_or_404(Superhero, name=hero_name)
            context = {
                'page_title': 'Hero Details',
                'hero': hero,
            }
            return render(request, 'hero_details.html', context)

    else:
        # unbound (empty) form
        formset = HeroFormSet()

        context = {
            'page_title': 'Form Example',
            'formset': formset,
        }
        return render(request, 'hero_select.html', context)
