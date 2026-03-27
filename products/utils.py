from products.forms import LaptopDetailsForm, ComputerDetailsForm, KeyboardDetailsForm, MouseDetailsForm, \
    HeadphonesDetailsForm, SpeakersDetailsForm
from products.models import ProductImage

DETAIL_FORM_CLASSES = {
    "laptop": LaptopDetailsForm,
    "computer": ComputerDetailsForm,
    "keyboard": KeyboardDetailsForm,
    "mouse": MouseDetailsForm,
    "headphones": HeadphonesDetailsForm,
    "speakers": SpeakersDetailsForm,
}

def get_product_details_forms(request=None, product=None):
    post_data = request.POST if request else None

    return {
        key: form_class(
            post_data,
            instance=getattr(product, key, None) if product else None,
            prefix=key
        )
        for key, form_class in DETAIL_FORM_CLASSES.items()
    }

def handle_product_form_submission(request, product_form_class, product_instance=None, require_images=True):
    uploaded_images = request.FILES.getlist("images")
    product_base_form = product_form_class(request.POST, request.FILES, instance=product_instance)
    product_details_forms = get_product_details_forms(request, product_instance)

    image_field_errors = []

    if require_images and not uploaded_images:
        image_field_errors.append("Please upload at least one image.")

    selected_category = request.POST.get("category")
    selected_details_form = product_details_forms.get(selected_category)

    if product_base_form.is_valid() and selected_details_form.is_valid() and not image_field_errors:
        product_base = product_base_form.save()
        product_details = selected_details_form.save(commit=False)
        product_details.product = product_base
        product_details.save()

        if uploaded_images:
            for image in uploaded_images:
                ProductImage.objects.create(
                    product=product_base,
                    image=image,
                )

        return {
            "is_valid": True,
            "product": product_base,
            "product_form": product_base_form,
            "product_details_forms": product_details_forms,
            "image_field_errors": image_field_errors,
        }

    return {
        "is_valid": False,
        "product": product_instance,
        "product_form": product_base_form,
        "product_details_forms": product_details_forms,
        "image_field_errors": image_field_errors,
    }