from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from products.forms import ProductCreateForm, ProductCategoryFilterForm, ProductSearchForm, LaptopDetailsForm, \
    HeadphonesDetailsForm, KeyboardDetailsForm, ComputerDetailsForm, MouseDetailsForm, SpeakersDetailsForm, ReviewForm
from products.models import Product, ProductImage
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

class AddProduct(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = ProductCreateForm
    model = Product
    template_name = 'products/add-product.html'
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
        uploaded_images = request.FILES.getlist("images")
        product_form = ProductCreateForm(request.POST, request.FILES)
        details_forms = get_product_details_forms(request)

        image_field_errors = []

        if not uploaded_images:
            image_field_errors.append("Please upload at least one image.")

        selected_category = request.POST.get("category")
        selected_form = details_forms.get(selected_category)

        if product_form.is_valid() and selected_form.is_valid() and uploaded_images:
            product = product_form.save()
            details = selected_form.save(commit=False)
            details.product = product
            details.save()

            for image in uploaded_images:
                ProductImage.objects.create(
                    product=product,
                    image=image,
                )

            return redirect("catalog")

        context = {
            "image_field_errors": image_field_errors,
            "product_form": product_form,
            "product_details_forms": details_forms,
        }

        return render(request, self.template_name, context)

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product-details.html'
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