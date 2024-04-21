from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)
