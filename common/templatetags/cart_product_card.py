from django import template

register = template.Library()

@register.inclusion_tag("components/cart-product-card.html")
def cart_product_card(name="", image="", price="", quantity="", slug=""):
    return {
        "name": name,
        "image": image,
        "price": price,
        "quantity": quantity,
        "slug": slug,
    }