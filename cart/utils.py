from django.conf import settings
from cart.models import Cart, CartItem
from products.models import Product


def get_cart(request):
    if request.user.is_authenticated:
        user_cart, _ = Cart.objects.get_or_create(user=request.user)
        return "user_cart", user_cart
    else:
        session_cart = request.session.get(settings.CART_SESSION_ID)
        if not session_cart:
            session_cart = request.session[settings.CART_SESSION_ID] = {}
        return "session_cart", session_cart

def merge_session_cart_into_user_cart(request, user):
    session_cart = request.session.get(settings.CART_SESSION_ID, {})

    if not session_cart:
        return

    user_cart, _ = Cart.objects.get_or_create(user=user)

    for product_id, quantity in session_cart.items():
        product = Product.objects.filter(pk=product_id).first()

        if not product:
            continue

        cart_item, created = CartItem.objects.get_or_create(
            cart=user_cart,
            product=product,
            defaults={"quantity": quantity},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    request.session[settings.CART_SESSION_ID] = {}
    request.session.modified = True