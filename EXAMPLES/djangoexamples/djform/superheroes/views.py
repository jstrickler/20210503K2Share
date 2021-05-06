"""
    Views for the DJForms Project

    These are forms illustrating how forms work in Django
"""
from django.shortcuts import get_object_or_404, render, redirect
from .forms import DemoForm, HeroForm, HeroModelForm, CityModelForm
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


def demoform(request):
    """
    Generic form demo with various fields

    :param request: HTTP request
    :return: HTTP Response
    """
    invalid = False

    if request.method == 'POST':  # if form filled out
        form = DemoForm(request.POST)
        if form.is_valid():
            # if data is valid, show results page
            context = {
                    'page_title': 'Form Fields Results',
                    'data': form.cleaned_data,
            }
            return render(request, 'form_results.html', context)
        else:
            # show form with errors for correcting
            invalid = True
    else:
        form = DemoForm() # unbound form

    # unless POST/valid, redraw form
    context = {
        'page_title': 'Form Fields Example',
        'form': form,
        'invalid': invalid,
    }
    return render(request, 'form_demo.html', context)


def heroform(request):
    """

    :param request: HTTP request
    :return: HTTP Response
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroForm(request.POST)
        if form.is_valid():
            hero_name = form.cleaned_data['hero_name']
            hero_color = form.cleaned_data['hero_color']
            request.session['color'] = hero_color
            hero = get_object_or_404(Superhero, name=hero_name)
            context = {
                'page_title': 'Hero Details',
                'hero': hero,
                'color': hero_color,
            }
            return render(request, 'hero_details.html', context)

    else:
        # unbound (empty) form
        form = HeroForm()

        context = {
            'page_title': 'Form Example',
            'form': form,
        }
        return render(request, 'hero_select.html', context)


def heromodel(request):
    """

    :param request: HTTP request
    :return: HTTP Response
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = HeroModelForm(request.POST)
        if form.is_valid():
            context = {
                'page_title': 'Hero Details',
                'name': form.cleaned_data['name'],
                'secret_identity': form.cleaned_data['secret_identity'],
                'real_name': form.cleaned_data['real_name'],
            }
            # form.save()
            return render(request, 'hero_model_results.html', context)

    else:
        # unbound (empty) form
        form = HeroModelForm()

        context = {
            'page_title': 'Form Example',
            'form': form,
        }
        return render(request, 'hero_model_select.html', context)

def cityform(request):
    """

    :param request: HTTP request
    :return: HTTP Response
    """

    # bound (filled-in) form
    if request.method == 'POST':
        form = CityModelForm(request.POST)
        if form.is_valid():
            # write request to DB or log here ...

            form.save()
            return redirect("superheroes:success")

    else:
        # unbound (empty) form
        form = CityModelForm()

        context = {
            'page_title': 'Form Example',
            'form': form,
        }
        return render(request, 'city_form.html', context)


def success(request):
    return render(request, 'success.html', context={})
