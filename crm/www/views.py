from django.shortcuts import render


def index(request):
    return render(request, "www/index.html")


def products(request):
    return render(request, "www/products.html")


def about(request):
    return render(request, "www/about.html")
