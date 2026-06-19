from django.urls import path
from . import views


urlpatterns = [

    # All services
    path(
        '',
        views.service_list,
        name='service_list'
    ),

    # Category wise services
    path(
        'category/<slug:slug>/',
        views.category_services,
        name='category_services'
    ),

    # Book service
    path(
        'book/<slug:slug>/',
        views.book_service,
        name='book_service'
    ),

    # Service detail (always keep LAST)
    path(
        '<slug:slug>/',
        views.service_detail,
        name='service_detail'
    ),

]
