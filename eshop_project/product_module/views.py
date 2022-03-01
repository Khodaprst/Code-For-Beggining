from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('-rating')
    number_of_products = products.count()
    average = products.aggregate(Avg('rating'))
    return render(request, 'product_module/product_list.html', {
        'products': products,
        'total_number_of_product':number_of_products,
        'average_ratings': average,
    })



def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {
        'product': product
    })
