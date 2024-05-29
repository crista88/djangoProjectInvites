from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_dashboard/', views.home_dashboard, name='home_dashboard'),
]