from django.conf import settings


def shared_context(request):
    """
    Add shared context to page context.
    """
    return {
        'main_grid': '',
        'page_grid': 'container_12',
        'sidebar_grid': '',
    }