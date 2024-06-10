from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Event, Task
from .forms import EventForm, TaskForm
from django.urls import reverse_lazy
from django.views.generic import ListView


class EventCreateView(View):
    template_name = 'eventplanner/event_create.html'

    def get(self, request, *args, **kwargs):
        event_form = EventForm()
        events = Event.objects.all()
        return render(request, self.template_name, {'event_form': event_form, 'events': events})

    def post(self, request, *args, **kwargs):
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('event_detail')
        events = Event.objects.all()
        return render(request, self.template_name, {'event_form': event_form, 'events': events})


# class EventListView(ListView):
#
#     template_name = 'eventplanner/event_list.html'
#
#     def get(self, request, *args, **kwargs):
#         events = Event.objects.all()
#         return render(request, self.template_name, {'events': events})


class EventDetailView(View):
    template_name = 'eventplanner/event_detail.html'

    def get(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        tasks_todo = Task.objects.filter(event=event, status='to_do')
        tasks_done = Task.objects.filter(event=event, status='done')
        task_form = TaskForm()
        context = {
            'event': event,
            'tasks_todo': tasks_todo,
            'tasks_done': tasks_done,
            'task_form': task_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.event = event
            task.save()
            return redirect('event_detail', pk=event.pk)
        tasks_todo = Task.objects.filter(event=event, status='To DO')
        tasks_done = Task.objects.filter(event=event, status='Done')
        context = {
            'event': event,
            'tasks_todo': tasks_todo,
            'tasks_done': tasks_done,
            'task_form': task_form,
        }
        return render(request, self.template_name, context)
