from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from cart.utils import get_cart
from cart.models import CartItem, Cart
from orders.models import Order, OrderItem
from products.models import Product


class CartView(TemplateView):
    template_name = 'cart/cart-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_type, cart = get_cart(self.request)

        if cart_type == 'user_cart':
            cart_products = cart.items.select_related('product').prefetch_related('product__images')
            context['cart_products'] = cart_products
        else:
            product_ids = map(int, cart.keys())
            products = Product.objects.filter(id__in=product_ids).prefetch_related("images")
            session_products = []

            for product in products:
                session_products.append({
                    "product": product,
                    "quantity": cart.get(str(product.id), 0),
                })

            context["cart_products"] = session_products

        return context

class AddToCartView(View):
    def post(self, request, product_slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=product_slug)
        cart_type, cart = get_cart(request)

        if cart_type == 'user_cart':
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
        else:
            product_id = str(product.id)
            if product_id in cart:
                cart[product_id] += 1
            else:
                cart[product_id] = 1
            request.session[settings.CART_SESSION_ID] = cart
            request.session.modified = True

        return redirect("product-details", product_slug=product.slug)

class RemoveFromCartView(View):
    def post(self, request, product_slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=product_slug)
        cart_type, cart = get_cart(request)

        if cart_type == "user_cart":
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.quantity -= 1

            if cart_item.quantity == 0:
                cart_item.delete()
            else:
                cart_item.save()
        else:
            product_id = str(product.id)
            cart[product_id] -= 1

            if cart[product_id] == 0:
                del cart[product_id]

            request.session[settings.CART_SESSION_ID] = cart
            request.session.modified = True

        return redirect("cart")

class RemoveAllFromCartView(View):
    def post(self, request, *args, **kwargs):
        cart_type, cart = get_cart(request)

        if cart_type == "user_cart":
            cart.items.all().delete()
        else:
            request.session[settings.CART_SESSION_ID] = {}
            request.session.modified = True

        return redirect("cart")

class CheckoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.select_related("product").all()

        order_total_price = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            user=request.user,
            total_price=order_total_price
        )

        order_item = [
            OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            for item in cart_items
        ]

        OrderItem.objects.bulk_create(order_item)
        cart_items.delete()
        return redirect('order-details', pk=order.pk)