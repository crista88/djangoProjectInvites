from django.urls import path

from howitworks import views

urlpatterns = [
    path('', views.howitworks, name='howitworks'),
    path('howitworks_dashboard/', views.howitworks_dashboard, name='howitworks_dashboard'),
]