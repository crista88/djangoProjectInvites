from django.shortcuts import render, get_object_or_404

from models.models import Model


# Create your views here.
def models_view(request):
    models = Model.objects.all()
    return render(request, 'models/models.html', {'models': models})


def model_detail_view(request, id):
    model = get_object_or_404(Model, id=id)
    return render(request, 'models/templates/template1.html', {'model': model})


