# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from randomword import RandomWord
from airports import AIRPORTS

rw = RandomWord()

# Create your views here.

def home(request):
    return render(request, 'words/home.html', context={
        'message': 'Some bootstrap examples using word lists',
    })

def homenoboot(request):
    return render(request, 'words/homenoboot.html', context={
        'message': "Welcome to the Words app"}
                  )

def layout(request):
    context = {
        'message': "Using Bootstrap Layout",
        'words': rw.get_random_word_list(9)
    }
    return render(request, 'words/layout.html', context=context)

def layoutloops(request):
    context = {
        'message': "Using Bootstrap Layout With Loops",
        'words': rw.get_random_word_list(24),
    }
    return render(request, 'words/layoutloops.html', context=context)

def cycle(request):
    context = {
        'message': "Using cycle tag",
        'words': rw.get_random_word_list(20)
    }
    return render(request, 'words/cycle.html', context=context)

def grid(request):
    context = {
        'message': "Bootstrap grid with different column widths",
        'airports': AIRPORTS,
    }
    return render(request, 'words/grid.html', context=context)

def alerts(request):
    context = {
        'message': "Bootstrap alerts examples",
    }
    return render(request, 'words/alerts.html', context=context)

def breadcrumbs(request):
    context = {
        'message': "Bootstrap breadcrumbs examples",
    }
    return render(request, 'words/breadcrumbs.html', context=context)
