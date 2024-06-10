from django.urls import path
from .views import EventCreateView, EventDetailView, mark_task_done

urlpatterns = [
    path('create-event/', EventCreateView.as_view(), name='create_event'),
    path('event-detail/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event-detail/<int:pk>/mark-task-done/<int:task_id>/', mark_task_done, name='mark_task_done'),

]
