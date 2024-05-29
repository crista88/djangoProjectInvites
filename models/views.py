# views.py al aplicației models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Model


def models_view(request):
    models = Model.objects.all()
    if request.user.is_authenticated:
        template_name = 'models/models_dashboard.html'
    else:
        template_name = 'models/models.html'
    return render(request, template_name, {'models': models})


@login_required
def models_view_dashboard(request):
    models = Model.objects.all()
    return render(request, 'models/models_dashboard.html', {'models': models})


def model_detail_view(request, id):
    model = get_object_or_404(Model, id=id)
    if request.user.is_authenticated:
        template_name = 'models/model_details_dashboard.html'
    else:
        template_name = 'models/model_detail.html'
    return render(request, template_name, {'model': model})



