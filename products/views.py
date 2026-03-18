from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.forms import ProductCreateForm, ProductCategoryFilterForm, ProductSearchForm, ReviewForm, \
    ProductEditForm
from products.helpers import handle_product_form_submission
from products.models import Product
from products.utils import get_product_details_forms


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

class AddProductView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProductCreateForm
    model = Product
    template_name = 'products/add-product-page.html'
    success_url = reverse_lazy('catalog')

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, *args, **kwargs):
        context = {
            "product_form": ProductCreateForm(),
            "product_details_forms": get_product_details_forms(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        result = handle_product_form_submission(request, ProductCreateForm, None, True)

        if result["is_valid"]:
            return redirect("catalog")

        return render(request, self.template_name, result)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-details-page.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'review_form': ReviewForm(),
        })

        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.to_product = product
            review.user = request.user
            review.save()
            return redirect('product-details', pk=product.pk)

        context = self.get_context_data(review_form=form)
        return self.render_to_response(context)

class ProductEditView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'products/edit-product-page.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context["product_form"] = context["form"]
        context["product_details_forms"] = get_product_details_forms(product=product)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        result = handle_product_form_submission(request, ProductEditForm, self.object, False)

        if result["is_valid"]:
            return redirect("product-details", product_slug=result["product"].slug)

        return render(request, self.template_name, result)

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs["product_slug"])
        product.delete()
        return redirect("catalog")