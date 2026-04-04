from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from orders.models import Order, StatusChoices


class OrderManagementMixin(LoginRequiredMixin, UserPassesTestMixin):
    model = Order

    def test_func(self):
        order = self.get_object()
        return order.user == self.request.user and order.status == StatusChoices.PENDING

    def get_order_context(self, form, order, context=None):
        context = context or {}
        context["form"] = form
        context["order"] = order
        context["order_items"] = order.items.select_related("product").all()
        context["total_price"] = order.total_price
        return context