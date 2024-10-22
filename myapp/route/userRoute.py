from django.urls import path
from myapp.controller import userController

urlpatterns = [
    path('api/users', userController.getUsers, name='user-list'),
]
