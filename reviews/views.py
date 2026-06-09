from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm

from products.models import Product


@login_required
def add_review(request, product_id):

    product = Product.objects.get(
        id=product_id
    )

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(
                commit=False
            )

            review.user = request.user
            review.product = product

            review.save()

    return redirect(
        'product_detail',
        pk=product.id
    )