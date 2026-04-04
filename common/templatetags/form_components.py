from django import template

register = template.Library()


@register.inclusion_tag("components/input.html")
def custom_input(field_id="", label="", value="", name="", input_type="text", placeholder="", errors=None, disabled=False, is_required=True):
    return {
        "id": field_id,
        "label": label,
        "value": value,
        "name": name,
        "type": input_type,
        "placeholder": placeholder,
        "errors": errors or [],
        "disabled": disabled,
        "is_required": is_required,
    }


@register.inclusion_tag("components/checkbox.html")
def custom_checkbox(field_id="", label="", name="", checked=False, errors=None, disabled=False):
    return {
        "id": field_id,
        "label": label,
        "name": name,
        "checked": checked,
        "errors": errors or [],
        "disabled": disabled,
    }


@register.inclusion_tag("components/select.html")
def custom_select(field_id="", label="", value="", name="", options=None, errors=None, disabled=False, is_required=True):
    return {
        "id": field_id,
        "label": label,
        "value": value,
        "name": name,
        "options": options,
        "errors": errors or [],
        "disabled": disabled,
        "is_required": is_required,
    }


@register.inclusion_tag("components/textarea.html")
def custom_textarea(field_id="", label="", value="", name="", placeholder="", rows=3, cols=6, errors=None, disabled=False, is_required=True):
    return {
        "id": field_id,
        "label": label,
        "value": value,
        "name": name,
        "placeholder": placeholder,
        "rows": rows,
        "cols": cols,
        "errors": errors or [],
        "disabled": disabled,
        "is_required": is_required,
    }


@register.inclusion_tag("components/file-input.html")
def custom_file_input(field_id="", label="", name="", multiple=False, errors=None, is_required=True):
    return {
        "id": field_id,
        "label": label,
        "name": name,
        "multiple": multiple,
        "errors": errors or [],
        "is_required": is_required,
    }