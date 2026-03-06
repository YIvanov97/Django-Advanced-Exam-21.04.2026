from django import template

register = template.Library()

@register.inclusion_tag("common/../../templates/components/category-card.html")
def category_card(label="", href="", is_disabled=False):
    return {
        "label": label,
        "href": href,
        "is_disabled": is_disabled,
    }