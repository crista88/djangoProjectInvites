from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def howitworks(request):
    return render(request, 'howitworks/howitworks.html')

