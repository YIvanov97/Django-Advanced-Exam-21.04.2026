from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.api.serializers import OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.prefetch_related('items__product')

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(user=self.request.user)