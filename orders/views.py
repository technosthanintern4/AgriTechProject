from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from cart.models import CartItem
from .models import Order, OrderItem
from django.contrib import messages



@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    if not cart_items:
        return redirect('cart')

    total = sum(
        item.subtotal()
        for item in cart_items
    )

    if request.method == 'POST':

        order = Order.objects.create(
            user=request.user,
            full_name=request.POST.get('full_name'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            total_amount=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()

        return redirect('order_success')

    return render(
        request,
        'orders/checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


def order_success(request):

    return render(
        request,
        'orders/order_success.html'
    )


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/order_history.html',
        {
            'orders': orders
        }
    )


@login_required
def order_detail(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    items = OrderItem.objects.filter(
        order=order
    )

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order,
            'items': items
        }
    )


@login_required
def cancel_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    if order.status == "Pending":
        order.status = "Cancelled"
        order.is_cancelled = True
        order.save()

        messages.success(
            request,
            "Order cancelled successfully."
        )

    return redirect('order_history')