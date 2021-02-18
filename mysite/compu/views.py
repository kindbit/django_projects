from django.shortcuts import render, redirect
from .forms import ComputerForm
from .models import Computer

def main(request):
    title = 'Welcome: This is the Home Page'
    context = {
    "title": title,
    }
    return render(request, "compu/main.html",context)

def computer_entry(request):
    title = 'Add Computer'
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/compu/computer_list')
    context = {
        "title": title,
        "form": form,
        }
    return render(request, "compu/computer_entry.html",context)

def computer_list(request):
    title = 'List of all computers'
    queryset = Computer.objects.all()
    context = {
    "title": title,
    "queryset": queryset,
    }
    return render(request, "compu/computer_list.html", context)
