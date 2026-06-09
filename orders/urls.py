from django.urls import path

from .views import (
    checkout,
    order_success,
    order_history,
    order_detail,
    cancel_order
)

urlpatterns = [

    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    path(
        'success/',
        order_success,
        name='order_success'
    ),

    path(
        'history/',
        order_history,
        name='order_history'
    ),

    path(
        'detail/<int:order_id>/',
        order_detail,
        name='order_detail'
    ),

    path(
        'cancel/<int:order_id>/',
        cancel_order,
        name='cancel_order'
    )

]