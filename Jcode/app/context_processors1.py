from app.models import Category,CategorySub,Member
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

def member_list(request):
    members=Member.objects.filter(user_id=request.user.id).first()
    context={
        'member_list':members
    }
    return context
