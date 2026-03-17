from products.forms import LaptopDetailsForm, ComputerDetailsForm, KeyboardDetailsForm, MouseDetailsForm, \
    HeadphonesDetailsForm, SpeakersDetailsForm


DETAIL_FORM_CLASSES = {
    "laptop": LaptopDetailsForm,
    "computer": ComputerDetailsForm,
    "keyboard": KeyboardDetailsForm,
    "mouse": MouseDetailsForm,
    "headphones": HeadphonesDetailsForm,
    "speakers": SpeakersDetailsForm,
}

def get_product_details_forms(request=None):
    post_data = request.POST if request else None

    return {
        key: form_class(post_data, prefix=key)
        for key, form_class in DETAIL_FORM_CLASSES.items()
    }