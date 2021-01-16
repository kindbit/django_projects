from django.views import View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.models import Ad
from ads.models import Comment
from ads.forms import CreateForm
from ads.forms import CommentForm

class AdListView(OwnerListView):
    model = Ad
    fields = ['title','text','price','owner','created_at','updated_at']
    success_url = reverse_lazy('ads:all')
    template_name = "ads/ad_list.html"

class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title','text','price','owner','created_at','updated_at']
    template_name = "ads/ad_detail.html"
    def get(self, request, pk) :
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

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
    fields = ['title', 'text', 'price','owner','created_at','updated_at', 'comments']
    success_url = reverse_lazy('ads:all')
    template_name = "ads/ad_confirm_delete.html"

def stream_file(request, pk) :
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        a = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=a)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    def get_success_url(self):
        ad = self.object.ad
        return reverse("ads:ad_detail", args=[ad.id])
