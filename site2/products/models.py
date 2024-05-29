# products/models.py
from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2) #(10,2)
    description = models.TextField()
    rating = models.IntegerField(max_length=5,default=5)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# pascal case 
# camel case 