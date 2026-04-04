from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse

from cart.models import Cart
from orders.choices.status_choices import StatusChoices
from orders.forms import OrderStatusUpdateForm, OrderEditForm, OrderDeleteForm, OrderCreateForm
from orders.mixins import OrderManagementMixin
from orders.models import Order, OrderItem

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

class OrderCreateView(LoginRequiredMixin, View):
    template_name = 'orders/create-order-page.html'

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.select_related("product").all()
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        user_data = {
            "first_name": request.user.profile.first_name or "",
            "last_name": request.user.profile.last_name or "",
        }

        form = OrderCreateForm(initial=user_data)

        context = {
            "form": form,
            "cart_items": cart_items,
            "total_price": total_price,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.select_related("product").all()
        order_total_price = sum(item.product.price * item.quantity for item in cart_items)
        form = OrderCreateForm(request.POST)

        if not form.is_valid():
            context = {
                "form": form,
                "cart_items": cart_items,
                "total_price": order_total_price,
            }
            return render(request, self.template_name, context)

        order = form.save(commit=False)
        order.user = request.user
        order.total_price = order_total_price
        order.save()

        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            for item in cart_items
        ]

        OrderItem.objects.bulk_create(order_items)
        cart_items.delete()
        return redirect('order-details', pk=order.pk)

class OrderEditView(OrderManagementMixin, UpdateView):
    form_class = OrderEditForm
    template_name = 'orders/edit-order-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_order_context(context["form"], self.object, context)

    def get_success_url(self):
        return reverse('order-details', kwargs={'pk': self.object.pk})

class OrderDeleteView(OrderManagementMixin, DeleteView):
    form_class = OrderDeleteForm
    template_name = "orders/delete-order-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        delete_form = self.form_class(instance=self.object)
        return self.get_order_context(delete_form, self.object, context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("orders")

class OrderStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    form_class = OrderStatusUpdateForm

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse('order-details', kwargs={'pk': self.object.pk})