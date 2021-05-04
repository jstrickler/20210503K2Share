from django.http import HttpResponse
from datetime import datetime

# home view  ("index.html" equivalent)
def home(request):
    timestamp = datetime.now().strftime("%I:%M %p on %B %d, %Y")
    return HttpResponse("Hello, Django World at {}".format(timestamp))
