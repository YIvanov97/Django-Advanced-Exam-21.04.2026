from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from products.models import Product
from products.utils import get_product_details_forms


class ProductManagementMixin(LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    slug_url_kwarg = "product_slug"

    def test_func(self):
        return self.request.user.is_staff

    def get_product_context(self, form, product, context=None):
        context = context
        context["product"] = product
        context["product_form"] = form
        context["product_details_forms"] = get_product_details_forms(product=product)
        return context