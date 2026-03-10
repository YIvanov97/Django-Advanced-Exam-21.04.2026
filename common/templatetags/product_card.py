from django import template

register = template.Library()

@register.inclusion_tag("components/product-card.html")
def product_card(href="", product_name="", image="", price=""):
    return {
        "href": href,
        "product_name": product_name,
        "image": image,
        "price": price,
    }