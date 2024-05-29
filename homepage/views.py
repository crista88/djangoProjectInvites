from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return home_dashboard(request)
    else:
        return render(request, 'homepage/home.html')


@login_required
def home_dashboard(request):
    return render(request, 'homepage/home_dashboard.html')