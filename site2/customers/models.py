from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    fullName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.PositiveIntegerField(max_length=13)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.fullName
    