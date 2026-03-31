from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse

from orders.choices.status_choices import StatusChoices
from orders.forms import OrderStatusUpdateForm
from orders.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')

class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'orders/order-details-page.html'
    context_object_name = 'order'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_status_choices"] = StatusChoices.choices
        return context

class OrderStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderStatusUpdateForm

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse('order-details', kwargs={'pk': self.object.pk})