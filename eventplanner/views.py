from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Budget, Expense, Task
from .forms import BudgetForm, ExpenseForm, TaskForm


@login_required
def event_planner(request):
    try:
        # Obținem sau creăm bugetul pentru utilizatorul curent
        budget, created = Budget.objects.get_or_create(user=request.user)
    except Budget.DoesNotExist:
        budget = Budget.objects.create(user=request.user, amount=0)

    # Filtrăm cheltuielile pentru bugetul utilizatorului curent
    expenses = Expense.objects.filter(budget=budget)

    # Filtrăm task-urile pentru utilizatorul curent
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'budget_submit' in request.POST:
            # Verificăm dacă a fost trimis formularul pentru buget
            budget_form = BudgetForm(request.POST, instance=budget)
            if budget_form.is_valid():
                # Salvăm obiectul Budget cu datele din formular
                budget_instance = budget_form.save(commit=False)
                budget_instance.user = request.user  # Asigurăm utilizatorul asociat cu bugetul
                budget_instance.save()
                return redirect('event_planner')  # Redirecționăm utilizatorul înapoi la pagina de planificare a evenimentelor

        elif 'expense_submit' in request.POST:
            # Verificăm dacă a fost trimis formularul pentru cheltuieli
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense_instance = expense_form.save(commit=False)
                expense_instance.budget = budget
                expense_instance.save()
                return redirect('event_planner')

        elif 'task_submit' in request.POST:
            # Verificăm dacă a fost trimis formularul pentru task-uri
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                task_instance = task_form.save(commit=False)
                task_instance.user = request.user
                task_instance.save()
                return redirect('event_planner')

    else:
        # Inițializăm form-urile cu sau fără datele existente din baza de date
        budget_form = BudgetForm(instance=budget)
        expense_form = ExpenseForm()
        task_form = TaskForm()

    return render(request, 'event_planner.html', {'budget': budget, 'expenses': expenses, 'tasks': tasks,
                                                   'budget_form': budget_form, 'expense_form': expense_form,
                                                   'task_form': task_form})
