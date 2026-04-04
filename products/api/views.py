from rest_framework import generics
from rest_framework.permissions import AllowAny

from products.models import Product
from products.api.serializers import ProductSerializer


class Catalog(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        product_name = self.request.GET.get("name")
        selected_category = self.request.GET.get("category")

        if product_name:
            queryset = queryset.filter(name__icontains=product_name)

        if selected_category:
            queryset = queryset.filter(category=selected_category)

        return queryset