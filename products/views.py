from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from products.forms import ProductCreateForm
from products.models import Product


class Catalog(ListView):
    model = Product
    template_name = 'products/catalog.html'

class AddProduct(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProductCreateForm
    model = Product
    template_name = 'products/add-product.html'
    success_url = reverse_lazy('catalog')

    def test_func(self):
        return self.request.user.is_staff