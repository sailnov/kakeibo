from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import urls, views

urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("<int:year>/<int:month>", views.MainView.as_view(), name="index"),
]