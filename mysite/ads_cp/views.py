from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class AdListView(OwnerListView):
    model = Ad
    fields = ['title','text','price','owner','created_at','updated_at']
    success_url = reverse_lazy('ads:all')
    # template_name = "ads/ad_list.html"

class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title','text','price','owner','created_at','updated_at']

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title','text','price','picture']
    success_url = reverse_lazy('ads:main')

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']
    success_url = reverse_lazy('ads:all')

class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields = ['title', 'text', 'price','owner','created_at','updated_at']
    success_url = reverse_lazy('ads:all')
