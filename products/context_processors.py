from .models import ProductCategory

def navbar_categories(request):
    try:
        categories = ProductCategory.objects.filter(
            is_active=True
        ).order_by('name')

    except Exception as e:
        print("Navbar categories error:", e)
        categories = []

    return {
        "navbar_categories": categories
    }