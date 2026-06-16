from django.urls import path

from .views import (
    book_consultation,
    consultation_success
)

urlpatterns = [

    path(
        'book/<int:doctor_id>/',
        book_consultation,
        name='book_consultation'
    ),

    path(
        'book/service/<slug:service_slug>/',
        book_consultation,
        name='book_service'
    ),

    path(
        'success/',
        consultation_success,
        name='consultation_success'
    ),

]