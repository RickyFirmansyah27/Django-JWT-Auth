from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.route.productRoute')), 
    path('', include('myapp.route.userRoute')), 
    path('', include('myapp.route.authRoute')), 
    path('admin/', admin.site.urls),
]
