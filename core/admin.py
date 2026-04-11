from django.contrib import admin
from .models import Category, Ministry, Event
from .models import HeroSlide

admin.site.register(Category)
admin.site.register(Ministry)
admin.site.register(Event)
admin.site.register(HeroSlide)