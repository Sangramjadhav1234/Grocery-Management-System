from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem, Order
from .forms import CheckoutForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key or request.session.create()
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        session_key=session_key,
        user=request.user if request.user.is_authenticated else None,
    )
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return render(request, 'add_to_cart.html', {'product': product, 'quantity': cart_item.quantity})

def cart_view(request):
    session_key = request.session.session_key or request.session.create()
    cart_items = CartItem.objects.filter(session_key=session_key)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart_view.html', {'cart_items': cart_items, 'total_price': total_price})

'''def checkout(request):
    session_key = request.session.session_key or request.session.create()
    cart_items = CartItem.objects.filter(session_key=session_key)
    if not cart_items.exists():
        return redirect('product_list')

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile_number = form.cleaned_data['mobile_number']
            order = Order.objects.create(
                name=name,
                mobile_number=mobile_number
            )
            order.items.set(cart_items)
            cart_items.delete()
            return redirect('generate_bill', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price, 'form': form})'''
def checkout(request):
    session_key = request.session.session_key or request.session.create()
    cart_items = CartItem.objects.filter(session_key=session_key)
    if not cart_items.exists():
        return redirect('product_list')

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile_number = form.cleaned_data['mobile_number']
            order = Order.objects.create(
                name=name,
                mobile_number=mobile_number
            )
            order.items.set(cart_items)
            cart_items.delete()
            return redirect('generate_bill', order_id=order.id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price, 'form': form})


def generate_bill(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = sum(item.product.price * item.quantity for item in order.items.all())
    return render(request, 'generate_bill.html', {'order': order, 'total_price': total_price})


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = sum(item.product.price * item.quantity for item in order.items.all())
    return render(request, 'order_confirm.html', {'order': order})

def order_confirmed(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = sum(item.product.price * item.quantity for item in order.items.all())
    return render(request, 'confirmed.html', {'order': order, 'total_price': total_price})
