from django import template

register = template.Library()

@register.inclusion_tag("components/button.html")
def button(
        icon="",
        label="Button",
        href="",
        button_type="button",
        color="transparent",
        background_color="transparent",
        is_outline=False,
        is_disabled=False,
        is_small=False,
        data_toggle="",
        data_target="",
        data_dismiss=""
):
    return {
        "icon": icon,
        "label": label,
        "href": href,
        "button_type": button_type,
        "color": color,
        "background_color": background_color,
        "is_outline": is_outline,
        "is_disabled": is_disabled,
        "is_small": is_small,
        "data_toggle": data_toggle,
        "data_target": data_target,
        "data_dismiss": data_dismiss,
    }