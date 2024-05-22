from django.urls import path

from howitworks import views

urlpatterns = [
    path('', views.howitworks, name='howitworks')
]