from cart.utils import get_cart

def cart_items_count(request):
    cart_type, cart = get_cart(request)

    if cart_type == "user_cart":
        count = sum(item.quantity for item in cart.items.all())
    else:
        count = sum(cart.values())

    return {
        "cart_items_count": count
    }