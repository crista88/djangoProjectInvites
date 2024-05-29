from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def howitworks(request):
    if request.user.is_authenticated:
        return howitworks_dashboard(request)
    else:
        return render(request, 'howitworks/howitworks.html')


@login_required
def howitworks_dashboard(request):
    return render(request, 'howitworks/howitworks_dashboard.html')