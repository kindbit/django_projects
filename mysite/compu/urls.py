from django.urls import path
from django.contrib import admin
from . import views

app_name='compu'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('cims', views.cims, name= 'cims'),
    path('computer_entry', views.computer_entry, name='computer_entry'),
    path('computer_list', views.computer_list, name='computer_list'),
    path('computer_list/<int:id>',views.computer_edit, name='computer_edit'),
    path('computer_list/<int:id>/delete',views.computer_delete, name='computer_delete'),
    ]
