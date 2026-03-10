from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from products.forms import ProductCreateForm, ProductCategoryFilterForm, ProductSearchForm
from products.models import Product


class Catalog(ListView):
    model = Product
    template_name = 'products/catalog.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        product_name = self.request.GET.get('name')
        selected_category = self.request.GET.get('category')

        if product_name:
            queryset = queryset.filter(name__icontains=product_name)

        if selected_category:
            queryset = queryset.filter(category=selected_category)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs.update({
            'category_filter_form': ProductCategoryFilterForm(),
            'search_form': ProductSearchForm()
        })
        return super().get_context_data(object_list=object_list, **kwargs)

class AddProduct(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProductCreateForm
    model = Product
    template_name = 'products/add-product.html'
    success_url = reverse_lazy('catalog')

    def test_func(self):
        return self.request.user.is_staff

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product-details.html'