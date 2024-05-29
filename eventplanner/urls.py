from django.urls import path

from eventplanner import views

urlpatterns = [
    path('', views.event_planner, name='event_planner')
]