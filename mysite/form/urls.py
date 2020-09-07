from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='form'
urlpatterns = [
    path('', TemplateView.as_view(template_name='form/main.html'), name='main'),
    path('example', views.example,name='example'),
    path('create', views.SimpleCreate.as_view(),name='create'),
    path('update', views.SimpleUpdate.as_view(),name='update'),
    path('validate', views.Validate.as_view(),name='validate'),
    path('meow', views.CatCreate.as_view(),'meow'),
    path('cat/<int:pk>/update', views.CatUpdate.as_view()),
    path('success', views.success, name='success'),
]
