from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.HomeCreateView.as_view(), name='home'),
]