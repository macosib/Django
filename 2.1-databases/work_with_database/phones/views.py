from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get('sort')
    sort_dict = {'name': 'name', 'min_price': 'price', 'max_price': "-price"}
    template = 'catalog.html'
    phones = Phone.objects.all().order_by(sort_dict.get(sort_param))
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {
        'phone': phone
    }
    return render(request, template, context)
