from django.urls import path
from publi.views import PublisherList
from . import views

urlpatterns = [
    path('publishers/', PublisherList.as_view()),
    path('', views.index, name='index'),
]
