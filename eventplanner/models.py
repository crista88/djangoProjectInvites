from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    budget = models.IntegerField()
    location = models.CharField(max_length=100) # vezi daca poti conecta cu google maps
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Event details {self.name}, {self.budget}, {self.location}, {self.date}'


class Task(models.Model):
    status_option = (
        ('TO DO', 'To DO'),
        ('DONE', 'Done')
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=status_option)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Task details {self.name}, {self.deadline}'
