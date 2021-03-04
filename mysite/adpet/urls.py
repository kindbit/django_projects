from django.urls import path, reverse_lazy
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

app_name='adpet'
urlpatterns = [
    #path('', TemplateView.as_view(template_name='adpet/main_menu.html'), name='main'),
    path('page1', TemplateView.as_view(template_name='adpet/main_menu.html'), name='page1'),
    path('adpet10', TemplateView.as_view(template_name='adpet/main_menu.html'), name='adpet10'),
    path('contact_us', TemplateView.as_view(template_name='adpet/contact_us.html'), name='contact_us'),
    path('all_dogs', views.AdListViewDogs.as_view(), name='all_dogs'),
    path('all_cats', views.AdListViewCats.as_view(), name='all_cats'),
    path('table', views.AdListViewTable.as_view(), name='table'),
    path('',                   views.AdListView.as_view(),   name = 'main'),
    path('adpet',                views.AdListView.as_view(), name = 'all'),
    path('ad/<int:pk>',        views.AdDetailView.as_view(), name = 'ad_detail'),
    path('ad/create',          views.AdCreateView.as_view(), name = 'ad_create'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(), name = 'ad_update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(), name = 'ad_delete'),
    path('ad/ad_picture/<int:pk>', views.stream_file,        name = 'ad_picture'),
]
