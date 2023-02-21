from django.urls import path,re_path
from . import views
from . import autocom
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('signup/', views.signup_view,name='signup'),
    path('profile/', views.profile_management,name='profile'),
    #path('product/autocomplete/', autocom.VideoAutocompleteView.as_view(), name='product-autocomplete'),
]