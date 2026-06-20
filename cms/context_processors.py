from django.urls import NoReverseMatch, reverse

from .models import FooterContent, MenuItem, WebsiteSettings


def _menu_url(item):
    if item.named_url:
        try:
            return reverse(item.named_url)
        except NoReverseMatch:
            return item.url or '#'
    return item.url or '#'


def cms_globals(request):
    settings = WebsiteSettings.objects.first()
    footer = FooterContent.objects.filter(is_active=True).first()
    menu_items = []

    parents = MenuItem.objects.filter(parent__isnull=True, is_enabled=True).order_by('sort_order', 'title')
    for item in parents:
        children = [
            {
                'title': child.title,
                'url': _menu_url(child),
                'open_in_new_tab': child.open_in_new_tab,
            }
            for child in item.children.filter(is_enabled=True).order_by('sort_order', 'title')
        ]
        menu_items.append({
            'title': item.title,
            'url': _menu_url(item),
            'open_in_new_tab': item.open_in_new_tab,
            'children': children,
        })

    return {
        'cms_settings': settings,
        'cms_footer': footer,
        'cms_menu_items': menu_items,
    }
