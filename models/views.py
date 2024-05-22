from django.shortcuts import render, get_object_or_404

from models.models import Model


# Create your views here.
def models_view(request):
    models = Model.objects.all()
    return render(request, 'models/models.html', {'models': models})


def model_detail_view(request, id):
    model = get_object_or_404(Model, id=id)
    return render(request, 'models/model_detail.html', {'model': model})


# def my_view(request):
#     models = Model.objects.all()
#     for model in models:
#         model.static_image_url = f"images/model_images/{model.name}.jpg"  # calea statică pentru fiecare obiect
#     return render(request, 'models/models.html', {'models': models})