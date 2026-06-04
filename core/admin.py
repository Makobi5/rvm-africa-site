from django.contrib import admin
from .models import Category, Ministry, Event,WeeklyProgram
from .models import HeroSlide,Leader,PageHeader,MinistryHighlight 

admin.site.register(Category)
admin.site.register(Ministry)
admin.site.register(Event)
admin.site.register(HeroSlide)
admin.site.register(WeeklyProgram)
admin.site.register(Leader) 
admin.site.register(PageHeader)
admin.site.register(MinistryHighlight)