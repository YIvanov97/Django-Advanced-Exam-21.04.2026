from django import template

register = template.Library()

@register.inclusion_tag("components/category-card.html")
def category_card(label="", category="", bg_image="", is_disabled=False):
    return {
        "label": label,
        "category": category,
        "bg_image": bg_image,
        "is_disabled": is_disabled,
    }