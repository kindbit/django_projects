from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.models import Ad, Comment
from ads.forms import CreateForm, CommentForm

class AdListView(OwnerListView):
    model = Ad
    fields = ['title','text','price','owner','created_at','updated_at', 'comments']
    success_url = reverse_lazy('ads:all')
    template_name = "ads/ad_list.html"

class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title','text','price','owner','created_at','updated_at', 'comments']
    template_name = "ads/ad_detail.html"


class AdCreateView(LoginRequiredMixin, View):
    model = Ad
    fields = ['title','text','price','picture']
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:main')
    def get(self, request, pk=None) :
        form = CreateForm()
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin, View):
    model = Ad
    fields = ['title', 'text', 'price', 'picture']
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')
    def get(self, request, pk) :
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = { 'form': form }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
    model = Ad
    fields = ['title', 'text', 'price','owner','created_at','updated_at']
    success_url = reverse_lazy('ads:all')
    template_name = "ads/ad_confirm_delete.html"

def stream_file(request, pk) :
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
