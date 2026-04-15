from django.contrib import admin
from .models import Category, Ministry, Event,WeeklyProgram
from .models import HeroSlide

admin.site.register(Category)
admin.site.register(Ministry)
admin.site.register(Event)
admin.site.register(HeroSlide)
admin.site.register(WeeklyProgram)