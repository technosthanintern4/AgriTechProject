from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def product_list(request):
    products = Product.objects.filter(
        is_available=True
    )

    return render(
        request,
        "products/product_list.html",
        {
            "products": products
        }
    )


def category_products(request, slug):

    category = get_object_or_404(
        ProductCategory,
        slug=slug,
        is_active=True
    )

    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    return render(
        request,
        "products/category_products.html",
        {
            "category": category,
            "products": products
        }
    )


def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug,
        is_available=True
    )

    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(
        id=product.id
    )[:4]

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "related_products": related_products
        }
    )