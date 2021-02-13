from django.urls import path
from django.contrib import admin
from . import views

app_name='compu'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('computer_entry', views.computer_entry, name='computer_entry'),
]
