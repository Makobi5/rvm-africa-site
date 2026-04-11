from django.shortcuts import render
from .models import Ministry, Event, HeroSlide

def home(request):
    slides = HeroSlide.objects.filter(is_active=True)
    ministries = Ministry.objects.all()
    events = Event.objects.all().order_by('-date')[:3]
    
    context = {
        'slides': slides,
        'ministries': ministries,
        'events': events,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
