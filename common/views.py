from django.shortcuts import render
from django.views.generic import TemplateView

from products.category_choices import CategoryChoices
from products.models import Product


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        existing_values = set(
            Product.objects.values_list("category", flat=True).distinct()
        )

        context["categories"] = [
            {
                "value": value,
                "label": label,
                "has_products": value in existing_values,
            }
            for value, label in CategoryChoices.choices
        ]

        return context


