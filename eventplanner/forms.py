
from django import forms
from .models import Event, Task


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'budget', 'location', 'date']

        # Optional: Customize the form widgets
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Budget'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'notes', 'deadline', 'status', 'price', 'supplier']

        # Optional: Customize the form widgets
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'supplier': forms.Textarea(attrs={'class': 'form-control'}),

        }

