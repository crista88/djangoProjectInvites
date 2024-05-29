from django.urls import path

from userextend import views

urlpatterns = [
    path('create_user', views.UserCreateView.as_view(), name='create-user'),
    path('login', views.UserLoginView.as_view(), name='login')
]