from django import template

register = template.Library()

@register.inclusion_tag("components/modal.html")
def modal(modal_id="", title="", subtitle="", action="", confirm_label="", cancel_label="", data_bs_dismiss=""):
    return {
        "modal_id": modal_id,
        "title": title,
        "subtitle": subtitle,
        "action": action,
        "confirm_label": confirm_label,
        "cancel_label": cancel_label,
        "data_bs_dismiss": data_bs_dismiss,
    }