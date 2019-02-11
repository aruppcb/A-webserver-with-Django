from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'index.html')

def display_HSC(request):
    items = HSC.objects.all()
    context = {
        'items': items,
        'header': 'HSC',
    }
    return render(request, 'index.html', context)


def display_PPC(request):
    items = PPC.objects.all()
    context = {
        'items': items,
        'header': 'PPC',
    }
    return render(request, 'index.html', context)


def display_Bidopt(request):
    items = Bidopt.objects.all()
    context = {
        'items': items,
        'header': 'Bidopt',
    }
    return render(request, 'index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_HSC(request):
    return add_item(request, HSCForm)


def add_PPC(request):
    return add_item(request, PPCForm)


def add_Bidopt(request):
    return add_item(request, BidoptForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_HSC(request, pk):
    return edit_item(request, pk, HSC, HSCForm)


def edit_PPC(request, pk):
    return edit_item(request, pk, PPC, PPCForm)


def edit_Bidopt(request, pk):
    return edit_item(request, pk, Bidopt, BidoptForm)


def delete_HSC(request, pk):

    template = 'index.html'
    HSC.objects.filter(id=pk).delete()

    items = HSC.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_PPC(request, pk):

    template = 'index.html'
    PPC.objects.filter(id=pk).delete()

    items = PPC.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_Bidopt(request, pk):

    template = 'index.html'
    Bidopt.objects.filter(id=pk).delete()

    items = Bidopt.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
