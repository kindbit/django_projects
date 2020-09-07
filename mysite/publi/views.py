from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from publi.models import Publisher

class PublisherList(ListView):
    model = Publisher
    template_name= 'publi/publisher_list.html'
    context_object_name = 'publisher_list'

def index(request):
    return render(request,'publi/main.html')
