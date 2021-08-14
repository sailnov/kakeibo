from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views, urls
from user import forms, views, urls


urlpatterns = [
    path('', include('app.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
]