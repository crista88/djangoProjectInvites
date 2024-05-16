from django.shortcuts import render
from django.views.generic import TemplateView


class HomeCreateView(TemplateView):
    template_name = 'homepage/home.html'
