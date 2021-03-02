from django.views import View
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from adpet.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from adpet.models import Ad
from adpet.forms import CreateForm

from django.contrib.humanize.templatetags.humanize import naturaltime
from well.utils import dump_queries
from django.db.models import Q

class AdListViewDogs(OwnerListView):
    model = Ad
    fields = ['title', 'specie', 'text','owner','created_at','updated_at', 'name','phone' ]
    success_url = reverse_lazy('adpet:all_dogs')
    template_name = "adpet/all_dogs.html"
    def get(self, request) :
        ad_list = Ad.objects.all()
        strval =  request.GET.get("search", False)

        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            query = Q(title__contains=strval)
            query.add(Q(text__contains=strval), Q.OR)
            objects = Ad.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            # try both versions with > 4 posts and watch the queries that happen
            objects = Ad.objects.all().order_by('-updated_at')[:10]
            # objects = Post.objects.select_related().all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'ad_list' : ad_list,  'ad_list' : objects, 'search': strval}
        retval = render(request, self.template_name, ctx)

        dump_queries()
        return retval;

class AdListViewCats(OwnerListView):
    model = Ad
    fields = ['title', 'specie', 'text','owner','created_at','updated_at', 'name','phone' ]
    success_url = reverse_lazy('adpet:all_cats')
    template_name = "adpet/all_cats.html"
    def get(self, request) :
        ad_list = Ad.objects.all()
        strval =  request.GET.get("search", False)

        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            query = Q(title__contains=strval)
            query.add(Q(text__contains=strval), Q.OR)
            objects = Ad.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            # try both versions with > 4 posts and watch the queries that happen
            objects = Ad.objects.all().order_by('-updated_at')[:10]
            # objects = Post.objects.select_related().all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'ad_list' : ad_list,  'ad_list' : objects, 'search': strval}
        retval = render(request, self.template_name, ctx)

        dump_queries()
        return retval;

class AdListView(OwnerListView):
    model = Ad
    fields = ['title', 'specie', 'text','owner','created_at','updated_at', 'name','phone' ]
    success_url = reverse_lazy('adpet:all')
    template_name = "adpet/ad_list.html"
    def get(self, request) :
        ad_list = Ad.objects.all()
        strval =  request.GET.get("search", False)

        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            query = Q(title__contains=strval)
            query.add(Q(text__contains=strval), Q.OR)
            objects = Ad.objects.filter(query).select_related().order_by('-updated_at')[:10]
        else :
            # try both versions with > 4 posts and watch the queries that happen
            objects = Ad.objects.all().order_by('-updated_at')[:10]
            # objects = Post.objects.select_related().all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'ad_list' : ad_list,  'ad_list' : objects, 'search': strval}
        retval = render(request, self.template_name, ctx)

        dump_queries()
        return retval;

class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title','text', 'specie','owner','created_at','updated_at']
    template_name = "adpet/ad_detail.html"
    def get(self, request, pk) :
        x = Ad.objects.get(id=pk)
        context = { 'ad' : x}
        return render(request, self.template_name, context)

class AdCreateView(LoginRequiredMixin, View):
    model = Ad
    fields = ['title','text', 'specie', 'breed', 'picture','name','phone']
    template_name = 'adpet/ad_form.html'
    success_url = reverse_lazy('adpet:main')
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
    fields = ['title','specie','specie', 'text',  'picture']
    template_name = 'adpet/ad_form.html'
    success_url = reverse_lazy('adpet:all')
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
    fields = ['title', 'specie','text', 'owner','created_at','updated_at']
    success_url = reverse_lazy('adpet:all')
    template_name = "adpet/ad_confirm_delete.html"

def stream_file(request, pk) :
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response

