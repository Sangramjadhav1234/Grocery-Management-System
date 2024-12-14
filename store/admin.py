from django.contrib import admin
from .models import Product, CartItem, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'session_key')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'mobile_number', 'created_at')
    search_fields = ('user__username', 'name', 'mobile_number')
    list_filter = ('created_at',)
