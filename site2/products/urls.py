# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # URL for product list view
    # You can add more URL patterns for other views if needed
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]
