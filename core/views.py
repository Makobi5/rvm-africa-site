from django.shortcuts import render,get_object_or_404
from .models import Ministry, Event, HeroSlide,WeeklyProgram,Event,Leader
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
    # We can fetch leaders here to show them at the bottom of the About page
    leaders = Leader.objects.all()
    return render(request, 'about.html', {'leaders': leaders})
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

def leadership(request):
    leaders = Leader.objects.all()
    return render(request, 'about/leadership.html', {'leaders': leaders})

def story_vision(request):
    return render(request, 'about/story_vision.html')

def founders_bio(request):
    return render(request, 'about/founders.html')

def faith_statement(request):
    return render(request, 'about/faith.html')
def church_detail(request):
    # Fetch programs to show in the "Weekly Gatherings" section
    programs = WeeklyProgram.objects.filter(is_active=True).order_by('order')
    return render(request, 'church_detail.html', {'programs': programs})
def worship_night(request):
    return render(request, 'ministries/annual_worship_night.html')

def worship_night(request):
    # Fetch the specific ministry by slug
    # Ensure you have set the slug to 'annual-worship-night' in the admin!
    ministry = get_object_or_404(Ministry, slug='annual-worship-night')
    highlights = ministry.highlights.all()
    
    return render(request, 'ministries/annual_worship_night.html', {
        'ministry': ministry,
        'highlights': highlights
    })