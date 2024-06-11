# urls.py al aplicației models
from django.urls import path
from . import views

urlpatterns = [
    path('', views.models_view, name='models'),
    path('models_dashboard/', views.models_view_dashboard, name='models_dashboard'),
    path('<int:id>/', views.model_detail_view, name='template'),
]
