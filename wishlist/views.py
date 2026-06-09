from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product


@login_required
def add_to_wishlist(request, product_id):

    product = Product.objects.get(
        id=product_id
    )

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect(
        'product_detail',
        pk=product.id
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