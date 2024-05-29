# products/urls.py
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import IndexView
from .views import cart_view,add_to_cart

urlpatterns = [
    path('show/', views.product_list, name='product_list'),  # URL for product list view
    # You can add more URL patterns for other views if needed
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    #renders templates but does not give dynamic datas
    path('lists/',TemplateView.as_view(template_name='index.html'), name='products'),
    path('',IndexView.as_view(),name='home'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
