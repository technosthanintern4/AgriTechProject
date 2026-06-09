from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category


def product_list(request):

    search = request.GET.get('search')
    category_id = request.GET.get('category')

    products = Product.objects.filter(
        is_available=True
    )

    if search:
        products = products.filter(
            name__icontains=search
        )

    if category_id:
        products = products.filter(
            category_id=category_id
        )

    categories = Category.objects.all()

    return render(
        request,
        'products/shop.html',
        {
            'products': products,
            'categories': categories,
        }
    )


def product_detail(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk
    )

    return render(
        request,
        'products/detail.html',
        {
            'product': product
        }
    )