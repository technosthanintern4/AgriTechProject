from django.contrib import admin
from .models import Service, ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'slug',
        'is_active'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'is_active',
        'created_at'
    )

    list_editable = (
        'is_active',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    search_fields = (
        'title',
        'description'
    )

    list_filter = (
        'category',
        'is_active',
        'created_at'
    )

    readonly_fields = (
        'created_at',
        'updated_at'
    )

    fieldsets = (

        ('Service Information', {
            'fields': (
                'category',
                'title',
                'slug',
                'description'
            )
        }),

        ('Image', {
            'fields': (
                'image',
            )
        }),

        ('Status', {
            'fields': (
                'is_active',
            )
        }),

        ('Timestamps', {
            'fields': (
                'created_at',
                'updated_at'
            )
        }),

    )