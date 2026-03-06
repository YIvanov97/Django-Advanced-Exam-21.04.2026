from django import template

register = template.Library()

@register.inclusion_tag("components/button.html")
def button(label="Button", href="", button_type="button", color="transparent", background_color="transparent", is_outline=False, is_disabled=False):
    return {
        "label": label,
        "href": href,
        "button_type": button_type,
        "color": color,
        "background_color": background_color,
        "is_outline": is_outline,
        "is_disabled": is_disabled,
    }