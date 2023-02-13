from app.models import Category,CategorySub
from django import template

def category_list(request):
    categories = Category.objects.all()
    category_subs = CategorySub.objects.all().order_by('category')
    context = {
        'category_list':categories,
        'subcategory_list':category_subs,
    }
    # Return a dictionary with the data you want to load
    # on every request call or every page.'
    return context

