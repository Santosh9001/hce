# categories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    # You can add more URL patterns for other views if needed
    # path('items/',views.category_products,name='category_products')
]
