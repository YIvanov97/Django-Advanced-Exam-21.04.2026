from django import template

register = template.Library()

@register.inclusion_tag("components/cart-product-card.html")
def cart_product_card(name="", image="", price="", quantity="", slug="", is_cart_view=True):
    return {
        "name": name,
        "image": image,
        "price": price,
        "quantity": quantity,
        "slug": slug,
        "is_cart_view": is_cart_view,
    }