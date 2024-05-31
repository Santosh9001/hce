# products/views.py
from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .forms import ProductForm
from .models import CartItem, Product, Cart
from .serializers import ProductSerializer
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def cart_view(request):
    cart_items_count = Cart.objects.count()  # Example logic to get cart items count
    return JsonResponse({'cart_items_count': cart_items_count})

@login_required
def add_to_cart(request, product_id):
    logger.info(f"Add to cart called with product_id: {product_id}")
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    cart_items_count = cart.items.count()
    return JsonResponse({'cart_items_count': cart_items_count})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products/product_list')  # Redirect to the product list view
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})