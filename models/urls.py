from django.urls import path

from models.views import models_view, model_detail_view

urlpatterns = [
    path('', models_view, name='models'),
    path('<int:id>/', model_detail_view, name='model_detail'),
]