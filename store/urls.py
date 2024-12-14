from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('generate_bill/<int:order_id>/', views.generate_bill, name='generate_bill'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('order_confirmed/<int:order_id>/', views.order_confirmed, name='order_confirmed'),
]
