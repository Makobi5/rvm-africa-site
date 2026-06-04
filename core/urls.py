from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/', views.events_list, name='events_list'),
    path('leadership/', views.leadership, name='leadership'),
    path('our-story/', views.story_vision, name='story_vision'),
    path('founders/', views.founders_bio, name='founders'),
    path('faith/', views.faith_statement, name='faith'),
    path('church-kirugu/', views.church_detail, name='church_detail'),
    path('annual-worship-night/', views.worship_night, name='worship_night'),
]