from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('reviews/', include('reviews.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('doctors/', include('doctors.urls')),
    path('consultations/', include('consultations.urls')),
    path('gardeners/', include('gardeners.urls')),
]