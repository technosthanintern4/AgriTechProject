from django.urls import path

from .views import (
    gardener_list,
    book_gardener,
    gardener_booking_success
)

urlpatterns = [

    path(
        '',
        gardener_list,
        name='gardener_list'
    ),

    path(
        'book/<int:gardener_id>/',
        book_gardener,
        name='book_gardener'
    ),

    path(
        'success/',
        gardener_booking_success,
        name='gardener_booking_success'
    ),

   

]