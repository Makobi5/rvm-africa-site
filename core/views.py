from django.shortcuts import render,get_object_or_404
from .models import Ministry, Event, HeroSlide,WeeklyProgram,Event
from django.utils import timezone
def home(request):
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    featured_ministries = Ministry.objects.filter(show_on_slider=True)
    programs = WeeklyProgram.objects.filter(is_active=True).order_by('order')
    
    # NEW: Fetch Events
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now, is_active=True).order_by('date')[:2]
    past_events = Event.objects.filter(date__lt=now, is_active=True).order_by('-date')[:4]
    
    context = {
        'slides': slides,
        'featured_ministries': featured_ministries,
        'programs': programs,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def events_list(request):
    now = timezone.now()
    # Get all active events, split by date
    upcoming = Event.objects.filter(date__gte=now, is_active=True).order_by('date')
    past = Event.objects.filter(date__lt=now, is_active=True).order_by('-date')
    
    return render(request, 'events.html', {
        'upcoming': upcoming,
        'past': past
    })

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})
