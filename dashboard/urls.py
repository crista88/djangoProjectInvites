from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home')
]