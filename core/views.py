from django.shortcuts import render
from .models import Ministry, Event

def home(request):
    # Fetch all ministries from the database
    ministries = Ministry.objects.all()
    # Fetch the 3 most recent events
    events = Event.objects.all().order_by('-date')[:3]
    
    context = {
        'ministries': ministries,
        'events': events,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
