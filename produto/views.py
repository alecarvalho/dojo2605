from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def categories(request):
    return render(request, 'categories.html')


def form_products(request):
    return render(request, 'form_products.html')

def form_categories(request):
    return render(request, 'form_categories.html')