from django.shortcuts import render
from .models import Ministry, Event, HeroSlide

def home(request):
    slides = HeroSlide.objects.filter(is_active=True).order_by('order')
    # Fetch ministries for the horizontal scroller
    featured_ministries = Ministry.objects.filter(show_on_slider=True)
    
    return render(request, 'index.html', {
        'slides': slides,
        'featured_ministries': featured_ministries,
    })
def about(request):
    return render(request, 'about.html')
