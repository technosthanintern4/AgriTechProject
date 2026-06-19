from django.contrib import admin
from .models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
        'is_active',
        'created_at'
    )

    list_filter = (
        'is_active',
        'created_at'
    )

    search_fields = (
        'name',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    readonly_fields = (
        'created_at',
        'updated_at'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'stock',
        'is_available'
    )

    list_filter = (
        'category',
        'is_available'
    )

    search_fields = (
        'name',
        'description'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    readonly_fields = (
        'created_at',
        'updated_at'
    )

    fieldsets = (

        ('Product Information', {
            'fields': (
                'category',
                'name',
                'slug',
                'description'
            )
        }),

        ('Image', {
            'fields': (
                'image',
            )
        }),

        ('Pricing', {
            'fields': (
                'price',
                'stock'
            )
        }),

        ('Availability', {
            'fields': (
                'is_available',
            )
        }),

        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at'
            )
        }),

    )