from django.urls import path
from .views import  EventCreateView, EventDetailView

urlpatterns = [
    path('create-event/', EventCreateView.as_view(), name='create_event'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    # path('event-list/', EventListView.as_view(), name='event_list'),

]
