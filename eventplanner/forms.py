from django import forms
from .models import Budget, Expense, Task


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'required': 'true'})  # marchează câmpul 'amount' ca obligatoriu


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'date']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'due_date']
