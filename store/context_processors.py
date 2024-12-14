from .models import CartItem

def cart_total_price(request):
    total_price = 0
    session_key = request.session.session_key
    if session_key:
        cart_items = CartItem.objects.filter(session_key=session_key)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
    return {'total_price': total_price}
    