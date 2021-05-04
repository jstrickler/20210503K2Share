from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render

# Create your views here.



# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to Sparkle Plenty")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Sparkle Plenty" }
#     return render(request, 'plenty/home.html', context)
