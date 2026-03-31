from django.views.generic import TemplateView

from products.choices.category_choices import CategoryChoices
from products.models import Product
class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

    CATEGORY_IMAGES = {
        'laptop': 'images/laptop.png',
        'computer': 'images/computer.png',
        'keyboard': 'images/keyboard.png',
        'mouse': 'images/mouse.png',
        'headphones': 'images/headphones.png',
        'speakers': 'images/speakers.png',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        existing_categories = (
            Product.objects.values_list("category", flat=True).distinct()
        )

        context["categories"] = [
            {
                "value": value,
                "label": label,
                "bg_image": self.CATEGORY_IMAGES.get(value),
                "has_products": value not in existing_categories,
            }
            for value, label in CategoryChoices.choices
        ]

        featured_products = Product.objects.order_by("-created_at")[:3]
        context["featured_products"] = featured_products

        return context
class AboutPageView(TemplateView):
    template_name = 'common/about-page.html'

class ContactPageView(TemplateView):
    template_name = "common/contact-page.html"