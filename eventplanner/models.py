from django.contrib.auth.models import User
from django.db import models


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)


    def __str__(self):
        return f'Budget for {self.user.username}'


class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.CharField(max_length=100)
    date = models.DateField()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
