from django.contrib import admin
from .models import ProductCategory, Product, ProductImage, ProductVariant


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


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
        'status',
        'is_available'
    )

    list_filter = (
        'category',
        'is_available',
        'status',
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
                'stock',
                'status'
            )
        }),

        ('Availability', {
            'fields': (
                'is_available',
            )
        }),

        ('SEO', {
            'fields': (
                'seo_title',
                'seo_description',
                'seo_keywords',
            )
        }),

        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at'
            )
        }),

    )

    inlines = (ProductImageInline, ProductVariantInline)
