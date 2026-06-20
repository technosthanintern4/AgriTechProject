from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product


@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect(
        'product_detail',
        slug=product.slug
    )


@login_required
def wishlist_view(request):

    items = Wishlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        'wishlist/wishlist.html',
        {
            'items': items
        }
    )
