from django.http import HttpResponseBadRequest
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
            return redirect('event_detail', pk=event_form.instance.pk)
        events = Event.objects.all()
        return render(request, self.template_name, {'event_form': event_form, 'events': events})

class EventDetailView(View):
    template_name = 'eventplanner/event_detail.html'

    def get(self, request, pk, *args, **kwargs):
        event = get_object_or_404(Event, pk=pk)
        tasks_todo = Task.objects.filter(event=event, status='TO DO')
        tasks_done = Task.objects.filter(event=event, status='DONE')
        task_form = TaskForm()
        last_task_done = Task.objects.filter(event=event, status='DONE').order_by('-updated_at').first()
        remaining_budget = event.budget - sum(task.price for task in tasks_done)
        context = {
            'event': event,
            'tasks_todo': tasks_todo,
            'tasks_done': tasks_done,
            'task_form': task_form,
            'last_task_done': last_task_done,
            'remaining_budget': remaining_budget,
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
        tasks_todo = Task.objects.filter(event=event, status='TO DO')
        tasks_done = Task.objects.filter(event=event, status='DONE')
        last_task_done = Task.objects.filter(event=event, status='DONE').order_by('-updated_at').first()
        remaining_budget = event.budget - sum(task.price for task in tasks_done)
        context = {
            'event': event,
            'tasks_todo': tasks_todo,
            'tasks_done': tasks_done,
            'task_form': task_form,
            'last_task_done': last_task_done,
            'remaining_budget': remaining_budget,
        }
        return render(request, self.template_name, context)

def mark_task_done(request, pk, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=task_id)
        if task.status != 'DONE':
            task.status = 'DONE'
            task.save()
            # Update event budget
            event = task.event
            event.budget -= task.price
            event.save()
        return redirect('event_detail', pk=pk)
    else:
        return HttpResponseBadRequest("Invalid Request")