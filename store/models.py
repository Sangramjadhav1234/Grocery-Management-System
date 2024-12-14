from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    items = models.ManyToManyField(CartItem)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id}'
