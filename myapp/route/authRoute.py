from django.urls import path
from myapp.controller import authController

urlpatterns = [
    path('api/v1/auth/register', authController.register, name='create auth'),
    path('api/v1/auth/login', authController.login, name='login'),
]
