from .models import Item

def categories(request):
    CATEGORY_CHOICES = Item._meta.get_field('category').choices
    return {'categories': CATEGORY_CHOICES}